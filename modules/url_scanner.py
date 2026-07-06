import requests
import time


def url_scanner():
    print("\n========== URL SCANNER ==========\n")

    url = input("Enter URL (https://example.com): ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        start = time.time()

        response = requests.get(url, timeout=10)

        end = time.time()

        print("\n========== RESULT ==========\n")

        print("🌐 URL          :", response.url)
        print("📡 Status Code  :", response.status_code)
        print("🖥 Server       :", response.headers.get("Server", "Unknown"))
        print("📄 Content Type :", response.headers.get("Content-Type", "Unknown"))
        print("🔒 HTTPS        :", "Yes" if response.url.startswith("https") else "No")
        print(f"⚡ Response Time : {(end-start):.2f} sec")

    except Exception as e:
        print("❌ Error:", e)
