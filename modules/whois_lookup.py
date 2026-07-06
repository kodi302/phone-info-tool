import whois


def whois_lookup():
    print("\n========== WHOIS LOOKUP ==========\n")

    domain = input("Enter Domain (example: google.com): ").strip()

    try:
        info = whois.whois(domain)

        print("\n========== RESULT ==========\n")

        print("🌐 Domain        :", info.domain_name)
        print("🏢 Registrar     :", info.registrar)
        print("📅 Created       :", info.creation_date)
        print("⏳ Expires       :", info.expiration_date)
        print("🔄 Updated       :", info.updated_date)
        print("📧 Emails        :", info.emails)
        print("🌍 Country       :", info.country)
        print("🖥 Name Servers  :", info.name_servers)

    except Exception as e:
        print("❌ Error:", e)
