import requests


def mac_lookup():
    print("\n========== MAC ADDRESS LOOKUP ==========\n")

    mac = input("Enter MAC Address (Example: 44:38:39:ff:ef:57): ").strip()

    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print("\n========== RESULT ==========\n")
            print("🖥️ MAC Address :", mac)
            print("🏢 Vendor      :", response.text)
        else:
            print("❌ Vendor not found or Invalid MAC Address.")

    except Exception as e:
        print("❌ Error:", e)
