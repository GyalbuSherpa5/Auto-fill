import pyperclip  # Required for clipboard operations

# dummy data
credentials = {
    "don@gmail.com": "i am don",
    "don1@gmail.com": "pass1",
    "don2@gmail.com": "pass2",
    "don3@gmail.com": "pass3"
}


def autofill():
    email = input("Enter your email: ")

    if email in credentials:
        password = credentials[email]
        pyperclip.copy(password)
        print("Password copied to clipboard. You can now paste it.")
    else:
        print("Email not found.")


def don():
    print("Gyalbu dai is don")


if __name__ == "__main__":
    autofill()
    don()
