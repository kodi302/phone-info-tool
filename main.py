import os
from colorama import Fore, init
from modules import system, cpu, memory, battery, storage, network, adb

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print(Fore.GREEN + """
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
PHONE INFORMATION TOOL (ADVANCED)
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
        elif choice == "0":
            break
        else:
            print("Invalid choice")

        input("\nPress Enter...")

menu()