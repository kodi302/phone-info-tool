import os
from colorama import Fore, init
from modules.export import export_json
from modules import  url_scanner
from modules import subdomain_scanner
from modules import password_checker
from modules import (
    system,
    cpu,
    memory,
    battery,
    storage,
    network,
    adb,
    phone_lookup,
    ip_lookup,
    imei,
    qr_generator,
    mac_lookup,
    dns_lookup,
    port_scanner,
    whois_lookup,
    ssl_checker,
    speed_test,
    username_checker,
    email_validator,
    hash_tool,
    password_generator,
    http_headers,
)

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(Fore.GREEN + """
╔══════════════════════════════════════════════╗
║                                              ║
║   ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗║
║   ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝║
║   ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ║
║   ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ║
║   ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗║
║   ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝║
║                                              ║
║         PHONE INFORMATION TOOL 🔥            ║
║                                              ║
╚══════════════════════════════════════════════╝
""")

def menu():
    while True:
        clear()
        banner()

        print(Fore.YELLOW + """
1. System Info
2. CPU Info
3. Memory Info
4. Battery Info
5. Storage Info
6. Network Info
7. ADB Devices
8. ADB Device Info
9. Phone Number Lookup
10. IP Address Lookup
11. IMEI Validator
12. QR Code Generator
13. MAC Address Lookup
14. DNS Lookup
15. Port Scanner
16. WHOIS Lookup
17. SSL Certificate Checker
18. Network Speed Test
19. Username Checker
20.email_validator
21.url_scanner
22.hash_tool
23.subdomain_scanner
24.password_checker
25.password_generator
26.http_headers,
0. Exit
""")

        choice = input(Fore.GREEN + "Enter choice: ")

        if choice == "1":
            system.get_system()
        elif choice == "2":
            cpu.get_cpu()
        elif choice == "3":
            memory.get_memory()
        elif choice == "4":
            battery.get_battery()
        elif choice == "5":
            storage.get_storage()
        elif choice == "6":
            network.get_network()
        elif choice == "7":
            adb.check_devices()
        elif choice == "8":
            adb.device_info()
        elif choice == "9":
            phone_lookup.phone_lookup()
        elif choice == "10":
            ip_lookup.ip_lookup()
        elif choice == "11":
            imei.imei_validator()
        elif choice == "12":
            qr_generator.generate_qr()
        elif choice == "13":
            mac_lookup.mac_lookup()
        elif choice == "14":
            dns_lookup.dns_lookup()
        elif choice == "15":
            port_scanner.port_scanner()
        elif choice == "16":
            whois_lookup.whois_lookup()
        elif choice == "17":
            ssl_checker.ssl_checker()
        elif choice == "18":
            speed_test.network_speed()
        elif choice == "19":
            username_checker.username_checker()
        elif choice == "20":
            email_validator.email_validator()
        elif choice == "21":
            url_scanner.url_scanner()
        elif choice == "22":
            hash_tool.hash_generator()
        elif choice == "23":
            subdomain_scanner.subdomain_scanner()
        elif choice == "24":
            password_checker.password_checker()
        elif choice == "25":
            password_generator.password_generator()
        elif choice == "26":
            http_headers.http_headers()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

        input("\nPress Enter...")

menu()
