import psutil
from colorama import Fore

def get_memory():
    mem = psutil.virtual_memory()
    print(Fore.CYAN + "\n[+] MEMORY INFO")
    print("Total:", round(mem.total / (1024**3), 2), "GB")
    print("Used:", round(mem.used / (1024**3), 2), "GB")