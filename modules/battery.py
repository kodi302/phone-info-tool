import psutil
from colorama import Fore

def get_battery():
    battery = psutil.sensors_battery()
    print(Fore.CYAN + "\n[+] BATTERY INFO")
    if battery:
        print("Percentage:", battery.percent, "%")
    else:
        print("Battery not available")