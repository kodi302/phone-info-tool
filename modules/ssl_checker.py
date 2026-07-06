import ssl
import socket
from datetime import datetime


def ssl_checker():
    print("\n========== SSL CERTIFICATE CHECKER ==========\n")

    domain = input("Enter Domain (example: google.com): ").strip()

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        print("\n========== CERTIFICATE INFO ==========\n")

        print("🌐 Domain       :", domain)
        print("🏢 Issuer       :", cert["issuer"][0][0][1])
        print("👤 Subject      :", cert["subject"][0][0][1])
        print("📅 Valid From   :", cert["notBefore"])
        print("⏳ Valid Until  :", cert["notAfter"])

        expiry = datetime.strptime(cert["notAfter"], "%b %d %H:%M:%S %Y %Z")
        remaining = (expiry - datetime.utcnow()).days

        print("📆 Days Left    :", remaining)

        if remaining > 30:
            print("✅ Certificate is Valid")
        else:
            print("⚠ Certificate Expiring Soon")

    except Exception as e:
        print("❌ Error:", e)
