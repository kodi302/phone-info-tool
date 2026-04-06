import psutil
from colorama import Fore

def get_cpu():
    print(Fore.CYAN + "\n[+] CPU INFO")
    print("Cores:", psutil.cpu_count())
    print("Usage:", psutil.cpu_percent(), "%")