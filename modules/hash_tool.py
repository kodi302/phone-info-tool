import hashlib


def hash_generator():
    print("\n========== HASH GENERATOR ==========\n")

    text = input("Enter Text: ")

    print("\n========== HASHES ==========\n")

    print("MD5     :", hashlib.md5(text.encode()).hexdigest())
    print("SHA1    :", hashlib.sha1(text.encode()).hexdigest())
    print("SHA256  :", hashlib.sha256(text.encode()).hexdigest())
    print("SHA512  :", hashlib.sha512(text.encode()).hexdigest())
