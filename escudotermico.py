#!/usr/bin/env python3
"""
Escudo Térmico - Otimizado para Redes
Um monitor de segurança para GPUs NVIDIA, focado em estabilidade e controle térmico.
Desenvolvido para ambientes Linux onde a performance e a segurança de hardware são prioridade.
"""

import subprocess
import time
import os
import sys

# --- CONFIGURAÇÕES ---
# Limite térmico de segurança em Celsius
TEMP_LIMIT = 87  
# Limite de energia em Watts (ajustado para performance/estabilidade)
POWER_LIMIT = 130
# Velocidade das ventoinhas (0 a 100)
FAN_SPEED = 85
# Lista de processos que devem ser finalizados em caso de emergência térmica
PROCESSOS_PARA_MATAR = ["ollama", "tradutor"] 

def set_gpu_policy():
    """Define as políticas de energia e ventoinhas via nvidia-smi e nvidia-settings."""
    try:
        subprocess.run(["sudo", "nvidia-smi", "-pl", str(POWER_LIMIT)], check=True)
        subprocess.run([
            "nvidia-settings", "-a", "[gpu:0]/GPUFanControlState=1", 
            "-a", "[fan:0]/GPUTargetFanSpeed=" + str(FAN_SPEED)
        ], check=True)
        print(f"[+] Política aplicada: {POWER_LIMIT}W | Fan em {FAN_SPEED}%.")
    except Exception as e:
        print(f"[!] Erro ao aplicar políticas: {e}")

def kill_processes():
    """Finaliza processos críticos para evitar danos ao hardware."""
    for proc in PROCESSOS_PARA_MATAR:
        os.system(f"pkill -f {proc}")
        print(f"[!] Comando de emergência enviado: {proc}")

def monitor():
    """Loop principal de monitoramento térmico."""
    print(f"[*] Monitorando temperatura (Limite: {TEMP_LIMIT}C)...")
    while True:
        try:
            cmd = ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"]
            temp_str = subprocess.check_output(cmd).decode().strip()
            temp = int(temp_str)
            
            if temp >= TEMP_LIMIT:
                print(f"\n[!!!] ALERTA CRÍTICO: {temp}C atingiu o limite!")
                kill_processes()
                sys.exit(1)
            
            print(f"Temperatura atual: {temp}C", end='\r')
            time.sleep(5)
        except KeyboardInterrupt:
            print("\n[*] Monitoramento encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"\n[!] Erro no monitoramento: {e}")
            break

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Erro: Este script exige privilégios de root (sudo).")
    else:
        set_gpu_policy()
        monitor()
