import time
import sys
from utils import clear_screen, print_banner, print_message
from network_scanner import scan_network, select_all_targets, select_target
from port_scanner import scan_ports
from vulnerability_scanner import scan_vulnerabilities

def loading_effect(text, duration=2):
    """Simula un proceso de carga con puntos suspensivos."""
    sys.stdout.write(f"{text}")
    for _ in range(duration * 3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)
    print(" done.")

def display_menu():
    """Muestra el menú principal con un diseño simple y profesional."""
    clear_screen()
    print_banner("Análisis de Vulnerabilidades de IoT", "red")

    print("\n[1] Escanear la Red")
    print("[2] Escanear Dispositivo")
    print("[3] Escanear Todos los Dispositivos")
    print("[4] Analizar Vulnerabilidades")
    print("[5] Generar Reporte")
    print("[6] Salir")

def main():
    while True:
        display_menu()
        choice = input("\nSeleccione una opción: ").strip()

        if choice == "1":
            print_message("Escaneando la red local.", "green")
            hosts = scan_network()
            loading_effect("Analizando dispositivos en la red")
            print_message("Escaneo finalizado.", "blue")
            input("\nPresione Enter para continuar.")

        elif choice == "2":
            hosts = scan_network()
            target = select_target(hosts)
            print_message(f"Escaneando puertos de {target}.", "green")
            open_ports = scan_ports(target)
            vulnerabilities = scan_vulnerabilities(target, open_ports)
            
            print_message("Escaneo finalizado.", "blue")
            input("\nPresione Enter para continuar.")

        elif choice == "3":
            print_message("Escaneando todos los dispositivos.", "green")
            hosts = scan_network()
            targets = select_all_targets(hosts)
            open_ports = scan_ports(targets)
            vulnerabilities = scan_vulnerabilities(targets, open_ports)
            print_message("Escaneo finalizado.", "blue")
            input("\nPresione Enter para continuar.")

        elif choice == "4":
            hosts = scan_network()
            target = select_target(hosts)
            open_ports = scan_ports(target)
            print_message("Analizando vulnerabilidades.", "green")
            vulnerabilities = scan_vulnerabilities(target, open_ports)
            print_message("Análisis completado.", "blue")
            input("\nPresione Enter para continuar.")

        elif choice == "5":
            hosts = scan_network()
            target = select_target(hosts)
            open_ports = scan_ports(target)
            vulnerabilities = scan_vulnerabilities(target, open_ports)
    
            input("\nPresione Enter para continuar.")

        elif choice == "6":
            print_message("Cerrando sesión.", "red")
            break

        else:
            print_message("Opción no válida. Intente de nuevo.", "red")
            input("\nPresione Enter para continuar.")

if __name__ == "__main__":
    main()
