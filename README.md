ThermalShield 🛡️

ThermalShield is a low-level automation and security tool designed to manage and protect hardware in high-performance workstations. Developed for Linux environments running intensive workloads—such as local LLMs, code compilation, or security audits—this script ensures your GPU remains within safe operational limits under heavy stress.
🚀 Key Features

This is not just a monitor; it is a fail-safe agent. It interfaces directly with NVIDIA drivers to:

    Enforce Power Policies: Sets rigid power consumption limits (Power Limit) to prevent unnecessary thermal spikes.

    Dynamic Fan Control: Manages hardware fan curves to optimize heat dissipation.

    Active Protection (Fail-safe): Monitors GPU temperature in real-time. If the configured safety threshold is reached, it automatically terminates critical processes to prevent permanent hardware damage.

🛠️ Tech Stack

    Language: Python 3.

    Integration: nvidia-smi and nvidia-settings.

    Focus: Low resource footprint and high reliability for production-grade environments.

⚙️ Installation and Usage
Requirements

    Linux OS (optimized for Debian-based systems).

    NVIDIA drivers properly installed and configured.

    Root privileges (sudo) to manage hardware settings.

Configuration

Edit the CONFIGURATIONS section at the beginning of thermal_shield.py to adjust TEMP_LIMIT, POWER_LIMIT, and the PROCESSOS_PARA_MATAR (processes to kill) list according to your needs.
Execution
Bash

sudo python3 thermal_shield.py
