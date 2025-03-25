import nmap
import socket
from utils import print_message

def scan_network():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    local_ip = ip[:10]

    nm = nmap.PortScanner()
    
    arguments = "-sn" 
    nm.scan(hosts=f"{local_ip}.0/24", arguments=arguments)
    

    hosts = nm.all_hosts()
    print_message("Hosts encontrados:", "green", attrs=["bold"])
    for i, host in enumerate(hosts):
        print(f"[{i}] {host}")

    return hosts

def select_target(hosts):
    while True:
        try:
            target_index = int(input(f"Introduce el número del host a escanear [0-{len(hosts)-1}]: "))
            if target_index < 0 or target_index >= len(hosts):
                raise ValueError
            return hosts[target_index]
        except ValueError:
            print_message("Entrada inválida. Por favor introduce un número válido.", "red", attrs=["bold"])
            
def select_all_targets(hosts):
    return hosts