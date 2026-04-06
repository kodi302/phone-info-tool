from colorama import Fore
import platform

def get_system():
    print(Fore.CYAN + "\n[+] SYSTEM INFO")
    print("OS:", platform.system(), platform.release())
    print("Processor:", platform.processor())