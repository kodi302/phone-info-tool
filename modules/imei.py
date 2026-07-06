def luhn_checksum(number):
    total = 0
    reverse = number[::-1]

    for i, digit in enumerate(reverse):
        n = int(digit)

        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9

        total += n

    return total % 10 == 0


def imei_validator():
    print("\n========== IMEI VALIDATOR ==========\n")

    imei = input("Enter 15-digit IMEI: ").strip()

    if not imei.isdigit():
        print("❌ IMEI must contain only numbers.")
        return

    if len(imei) != 15:
        print("❌ IMEI must be exactly 15 digits.")
        return

    if luhn_checksum(imei):
        print("\n✅ Valid IMEI Number")
    else:
        print("\n❌ Invalid IMEI Number")
