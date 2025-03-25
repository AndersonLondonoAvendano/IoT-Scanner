import os
from datetime import datetime

def ensure_logs_directory_exists():
    """Asegura que el directorio de logs exista."""
    if not os.path.exists("./logs"):
        os.makedirs("./logs")

def log_scan_start(target, port_range):
    """Registra el inicio de un escaneo en el archivo de log."""
    ensure_logs_directory_exists()
    with open(f"./logs/{target}_scan.log", "a") as f:
        f.write(f"Escaneo iniciado el {datetime.now()}\n")
        f.write(f"Escaneando el host {target} en el rango de puertos {port_range}\n")

def log_port_status(target, port, status):
    """Registra el estado de un puerto en el archivo de log."""
    ensure_logs_directory_exists()
    with open(f"./logs/{target}_scan.log", "a") as f:
        if status == "abierto":
            f.write(f"El puerto {port} está abierto\n")
        else:
            pass  # No se registra si el puerto está cerrado

def log_vulnerabilities(target, vulnerabilities):
    """Registra las vulnerabilidades encontradas en el archivo de log."""
    ensure_logs_directory_exists()
    with open(f"./logs/{target}_scan.log", "a") as f:
        f.write(f"Vulnerabilidades encontradas el {datetime.now()}\n")
        f.write(vulnerabilities)