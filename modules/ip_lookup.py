import requests


def ip_lookup():
    print("\n========== IP ADDRESS LOOKUP ==========\n")

    ip = input("Enter IP Address: ").strip()

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "success":
            print("\n❌ Invalid IP Address")
            return

        print("\n========== RESULT ==========\n")
        print("🌍 Country   :", data.get("country"))
        print("🏙️ City      :", data.get("city"))
        print("📍 Region    :", data.get("regionName"))
        print("📮 ZIP       :", data.get("zip"))
        print("🏢 ISP       :", data.get("isp"))
        print("🕒 Timezone  :", data.get("timezone"))
        print("🌐 Latitude  :", data.get("lat"))
        print("🌐 Longitude :", data.get("lon"))

    except Exception as e:
        print("\n❌ Error:", e)
