import re


def email_validator():
    print("\n========== EMAIL VALIDATOR ==========\n")

    email = input("Enter Email Address: ").strip()

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(pattern, email):
        print("\n✅ Valid Email Address")
    else:
        print("\n❌ Invalid Email Address")
