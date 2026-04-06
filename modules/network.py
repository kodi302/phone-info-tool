import psutil
from colorama import Fore

def get_network():
    print(Fore.CYAN + "\n[+] NETWORK INFO")
    addrs = psutil.net_if_addrs()
    for interface, addr in addrs.items():
        print(f"\nInterface: {interface}")
        for a in addr:
            print(" Address:", a.address)