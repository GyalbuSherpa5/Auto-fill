import sqlite3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

secret_key = 'x8A3zLb9Wc7Rf5Mp'


# Function to create a database table
def create_table():
    conn = sqlite3.connect('esewa_password_manager.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS password
                 (url TEXT, username TEXT, password TEXT)''')
    conn.commit()
    conn.close()


# Function to add a new entry to the database
def add_entry(url, username, password):
    # Encrypting the password before storing
    encrypted_password = encrypt_password(password, secret_key)

    conn = sqlite3.connect('esewa_password_manager.db')
    c = conn.cursor()
    c.execute("INSERT INTO password VALUES (?, ?, ?)", (url, username, encrypted_password))
    conn.commit()
    conn.close()
    print("Entry added successfully!")


# Function to retrieve saved passwords
def retrieve_passwords(url=None, email=None):
    conn = sqlite3.connect('esewa_password_manager.db')
    c = conn.cursor()

    if url and email:
        c.execute("SELECT * FROM password WHERE url=? AND username=?", (url, email))
    elif url:
        c.execute("SELECT * FROM password WHERE url=?", (url,))
    elif email:
        c.execute("SELECT * FROM password WHERE username=?", (email,))
    else:
        c.execute("SELECT * FROM password")

    passwords = c.fetchall()
    conn.close()

    if not passwords:
        print("No passwords saved yet.")
    else:
        print("\nUrl\t\tUsername\tPassword")
        for row in passwords:
            # Decrypting the password before displaying
            decrypted_password = decrypt_password(row[2], secret_key)
            print("{}\t\t{}\t\t{}".format(row[0], row[1], decrypted_password))

        return passwords


# Function to encrypt plaintext password
def encrypt_password(password, secret_key):
    cipher = AES.new(secret_key.encode(), AES.MODE_ECB)
    padded_password = pad(password.encode(), AES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    return base64.b64encode(encrypted_password).decode()


# Function to decrypt encrypted password
def decrypt_password(encrypted_password, secret_key):
    cipher = AES.new(secret_key.encode(), AES.MODE_ECB)
    decrypted_password = cipher.decrypt(base64.b64decode(encrypted_password))
    return unpad(decrypted_password, AES.block_size).decode()


def main():
    create_table()
    while True:
        print("\n1. Add new entry")
        print("2. Retrieve passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            url = input("Enter url: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            add_entry(url, username, password)

        elif choice == '2':
            url = input("Enter url: ")
            username = input("Enter username: ")

            retrieve_passwords(url, username)

            # if not passwords:
            #     print("No passwords saved yet.")
            # else:
            #     print("\nUrl\t\tUsername\tPassword")
            #     for row in passwords:
            #         # Decrypting the password before displaying
            #         decrypted_password = decrypt_password(row[2], secret_key)
            #         print("{}\t\t{}\t\t{}".format(row[0], row[1], decrypted_password))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
