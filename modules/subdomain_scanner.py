import requests


def subdomain_scanner():
    print("\n========== SUBDOMAIN SCANNER ==========\n")

    domain = input("Enter Domain (example: google.com): ").strip()

    subdomains = [
        "www",
        "mail",
        "ftp",
        "blog",
        "api",
        "dev",
        "test",
        "admin",
        "portal",
        "vpn",
        "m",
        "shop",
        "cdn",
        "ns1",
        "ns2",
        "smtp",
        "webmail",
    ]

    found = []

    for sub in subdomains:
        url = f"https://{sub}.{domain}"

        try:
            r = requests.get(url, timeout=3)

            if r.status_code < 400:
                found.append(url)

        except:
            pass

    print("\n========== RESULT ==========\n")

    if found:
        for site in found:
            print("✅", site)
    else:
        print("❌ No common subdomains found.")
