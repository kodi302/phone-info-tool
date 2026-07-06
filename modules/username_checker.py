import requests


def username_checker():
    print("\n========== USERNAME CHECKER ==========\n")

    username = input("Enter Username: ").strip()

    websites = {
        "GitHub": f"https://github.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://x.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
    }

    print("\nChecking...\n")

    for site, url in websites.items():
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print(f"✅ {site:<12} Found")
            else:
                print(f"❌ {site:<12} Not Found")

        except:
            print(f"⚠ {site:<12} Error")
