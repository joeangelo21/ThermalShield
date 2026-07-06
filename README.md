Escudo Térmico 🛡️

O Escudo Térmico é uma ferramenta de automação e segurança de baixo nível, projetada para gerenciar e proteger o hardware de estações de trabalho de alto desempenho. Desenvolvido para ambientes Linux que executam cargas intensivas (como modelos de linguagem local, compilação de código ou auditorias de segurança), este script garante que sua GPU operando sob estresse se mantenha dentro dos limites operacionais seguros.
🚀 O que ele faz?

Este não é apenas um monitor; é um agente de fail-safe. Ele atua diretamente na camada de driver da NVIDIA para:

    Aplicar Políticas de Energia: Define limites rígidos de consumo (Power Limit) para evitar picos de temperatura desnecessários.

    Controle Dinâmico de Ventilação: Gerencia a curva de ventilação do hardware para otimizar a dissipação de calor.

    Proteção Ativa (Fail-safe): Monitora a temperatura em tempo real. Caso o limite de segurança configurado seja atingido, ele encerra automaticamente processos críticos configurados, evitando danos permanentes ao hardware.

🛠️ Tecnologias

    Linguagem: Python 3.

    Integração: nvidia-smi e nvidia-settings.

    Foco: Baixo consumo de recursos e alta confiabilidade em ambientes de produção.

⚙️ Instalação e Uso

    Requisitos:

        Sistema Linux (testado e otimizado para MATE/Debian-based).

        Drivers NVIDIA instalados e configurados.

        Privilégios de superusuário (sudo).

    Configuração:
    Edite a seção de CONFIGURAÇÕES no início do script escudotermico.py para ajustar o TEMP_LIMIT, POWER_LIMIT e a lista de processos que deseja monitorar.

    Execução:
    Bash

    sudo python3 escudotermico.py
