import requests


def http_headers():
    print("\n========== HTTP HEADERS ANALYZER ==========\n")

    url = input("Enter URL: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        response = requests.get(url, timeout=10)

        print("\n========== HEADERS ==========\n")

        for key, value in response.headers.items():
            print(f"{key:<25}: {value}")

    except Exception as e:
        print("❌ Error:", e)
