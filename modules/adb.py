import os
from colorama import Fore

def check_devices():
    print(Fore.CYAN + "\n[+] Connected Devices")
    os.system("adb devices")

def device_info():
    print(Fore.CYAN + "\n[+] Device Info")
    os.system("adb shell getprop ro.product.model")