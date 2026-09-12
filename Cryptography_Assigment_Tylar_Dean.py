import hashlib

# SHA-256 TEXT HASHING

def hash_text():
    """Generate a SHA-256 hash from uder entered text."""

    text = input("\nEnter text to hash: ")

    # Convert the text ti bytes and generate its SHA-256 hash
    hash_result = hashlib.sha256(text.encode("utf-8")).hexdigest()

    print("\nSHA-256 Hash:")
    print(hash_result)


# SHA-256 FILE HASHING

def hash_file():
    """Generate a SHA-256 hash for a file."""

    file_name = input("\nEnter the file name: ")

    try:
        # Create a new SHA-256 hashing object
        sha256_hash = hashlib.sha256()

        # Open the file in binary read mode
        with open(file_name, "rb") as file:

            # Read the file in small pieces
            while True:
                chunk = file.read(4096)

                # Stop when there is no more data
                if not chunk:
                    break

                # Add the current piece of the filr to the hash
                sha256_hash.update(chunk)

        print("\nSHA-256 File Hash:")
        print(sha256_hash.hexdigest())

    except FileNotFoundError:
        print("\nError: File not found.")


# CAESAR CIPHER

def caesar_cipher(text, shift):
    """
    Shift letters through the alphabet using a Caesar cipher.
    Positive shifts encrypt and neative shifts decrypt.
    """

    result = ""

    for character in text:

        # Handle uppercase letters
        if character.isupper():
            shifted = (ord(character) - ord("A") + shift) % 26
            result += chr(shifted + ord("A"))

        # Handle lowercase letters
        elif character.islower():
            shifted = (ord(character) - ord("a") + shift) % 26
            result += chr(shifted + ord("a"))

        # Keep spaces, numbers, and punctuation unchanged
        else:
            result += character

    return result

# CAESAR CIPHER ENCRYPTION

def encrypt_message():
    """Encrypt a message using a Caesar cipher."""

    text = input("\nEnter tect to encrypt: ")

    try:
        shift = int(input("Enter shift amount: "))

        encrypted = caesar_cipher(text, shift)

        print("\nEncrypted Message:")
        print(encrypted)

    except ValueError:
        print("\nError: Shift amount must be a number.")

# CEASAR CIPHER DECRYPTION

def decrypt_message():
    """Decrypt a message using a Caesar cipher."""

    text = input("\nEnter text to decrypt: ")

    try:
        shift = int(input("Enter text to decrypt: "))

        # Using a negative shift reverses the encryption
        decrypted = caesar_cipher(text, -shift)

        print("\nDecryted Message:")
        print(decrypted)

    except ValueError:
        print("\nErrorL Shift amount must be number.")

# MAIN MENU

def main():
    """Display the main program menu."""

    while True:

        print("\n==================================")
        print("    CRYPTOGRAPHY ASSIGNMENT")
        print("==================================")

        print("1. SHA-256 Hash Text")
        print("2. SHA-256 Hash File")
        print("3. Caesar Cipher - Encrypt")
        print("4. Caesar Cipher - Decrypt")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            hash_text()

        elif choice == "2":
            hash_file()

        elif choice == "3":
            encrypt_message()

        elif choice == "4":
            decrypt_message()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice. Please choose a number from 1-5.")

# START PROGRAM

if __name__ == "__main__":
    main()