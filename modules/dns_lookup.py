import socket


def dns_lookup():
    print("\n========== DNS LOOKUP ==========\n")

    domain = input("Enter Domain (example: google.com): ").strip()

    try:
        ip = socket.gethostbyname(domain)

        print("\n========== RESULT ==========\n")
        print(f"🌍 Domain : {domain}")
        print(f"📡 IPv4   : {ip}")

        try:
            ipv6 = socket.getaddrinfo(domain, None, socket.AF_INET6)
            if ipv6:
                print(f"🌐 IPv6   : {ipv6[0][4][0]}")
        except:
            print("🌐 IPv6   : Not Available")

    except Exception as e:
        print("\n❌ Error:", e)
