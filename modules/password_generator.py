import random
import string


def password_generator():
    print("\n========== PASSWORD GENERATOR ==========\n")

    try:
        length = int(input("Enter Password Length (8-64): "))

        if length < 8:
            print("❌ Minimum length should be 8")
            return

        characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}<>?"

        password = "".join(random.choice(characters) for _ in range(length))

        print("\n========== GENERATED PASSWORD ==========\n")
        print(password)

    except ValueError:
        print("❌ Please enter a valid number.")
