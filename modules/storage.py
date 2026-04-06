import psutil
from colorama import Fore

def get_storage():
    disk = psutil.disk_usage('/')
    print(Fore.CYAN + "\n[+] STORAGE INFO")
    print("Total:", round(disk.total / (1024**3), 2), "GB")
    print("Used:", round(disk.used / (1024**3), 2), "GB")