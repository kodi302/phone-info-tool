import qrcode


def generate_qr():
    print("\n========== QR CODE GENERATOR ==========\n")

    data = input("Enter text / URL / phone number: ").strip()

    if not data:
        print("❌ No data entered")
        return

    filename = "qrcode.png"

    img = qrcode.make(data)
    img.save(filename)

    print(f"\n✅ QR Code saved as: {filename}")
