import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from modules.export import export_json


def phone_lookup():
    print("\n========== PHONE NUMBER LOOKUP ==========\n")

    number = input("Enter Phone Number (with country code): ")

    try:
        parsed = phonenumbers.parse(number)

        if not phonenumbers.is_valid_number(parsed):
            print("\n❌ Invalid Phone Number")
            return

        phone_number = phonenumbers.format_number(
            parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL
        )

        country = geocoder.description_for_number(parsed, "en")
        sim_carrier = carrier.name_for_number(parsed, "en")
        time_zone = ", ".join(timezone.time_zones_for_number(parsed))

        print("\n========== RESULT ==========\n")
        print("📱 Number      :", phone_number)
        print("🌍 Country     :", country)
        print("📡 Carrier     :", sim_carrier)
        print("🕒 Time Zone   :", time_zone)
        print("✅ Valid Number")

        data = {
            "Number": phone_number,
            "Country": country,
            "Carrier": sim_carrier,
            "Timezone": time_zone,
        }

        save = input("\nExport Report? (y/n): ").strip().lower()

        if save == "y":
            export_json(data, "phone_report.json")

    except Exception as e:
        print("\n❌ Error:", e)
