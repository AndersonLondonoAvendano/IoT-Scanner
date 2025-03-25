import os
import socket
from tqdm import tqdm
from utils import print_message
from logger import log_scan_start, log_port_status

def scan_ports(targets):
    """
    Escanea los puertos en los objetivos especificados utilizando la configuración más rápida, potente y menos detectable.

    :param targets: Lista de direcciones IP o una sola dirección IP.
    :return: Diccionario que mapea cada IP a una lista de puertos abiertos.
    """
    # Convertir targets en una lista si es un solo string
    if isinstance(targets, str):
        targets = [targets]
    
    
    timeout = 0.05 
    
    # Crear el directorio de logs si no existe
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Solicitar el rango de puertos a escanear
    while True:
        try:
            port_range = input("Introduce el rango de puertos a escanear [ej. 1-65536]: ")
            start_port, end_port = map(int, port_range.split("-"))
            total_ports = end_port - start_port + 1

            if port_range.count("-") != 1 or start_port < 1 or end_port > 65536 or start_port > end_port:
                raise ValueError
            
            break
        except ValueError:
            print_message("Entrada inválida. Introduce un rango de puertos válido [ej. 1-65536].", "red", attrs=["bold"])

    # Inicializar el archivo de log
    all_open_ports = {}  # Diccionario para almacenar los puertos abiertos por target

    for target in targets:
        open_ports = []  # Lista de puertos abiertos para el target actual
        print_message(f"\nEscaneando el host {target} en el rango de puertos {port_range}", "green", attrs=["bold"])
        log_scan_start(target, port_range)

        # Barra de progreso para el escaneo
        with tqdm(total=total_ports, desc=f"Progreso [{target}]", unit="puerto", ncols=80, bar_format="{l_bar}{bar}{r_bar}", colour="red") as pbar:
            for port in range(start_port, end_port + 1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(timeout)  # Configurar el tiempo de espera para escaneo rápido y sigiloso
                    result = s.connect_ex((target, port))
                    if result == 0:
                        open_ports.append(port)
                        log_port_status(target, port, "abierto")
                    else:
                        log_port_status(target, port, "cerrado")
                    pbar.update(1)

        all_open_ports[target] = open_ports  # Almacenar los puertos abiertos para este target

        # Mostrar resultados del escaneo
        if open_ports:
            print_message(f"\nPuertos abiertos en {target}:", "red", attrs=["bold"])
            print('\n'.join(map(str, open_ports)))
        else:
            print_message(f"\nNo se encontraron puertos abiertos en {target}.", "green", attrs=["bold"])
    
    #print(all_open_ports)
    return all_open_ports
