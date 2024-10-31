def caesar_cipher(text, key, mode):
    result = ""
    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    for char in text:
        if 'A' <= char <= 'Z':
            # Encrypting
            if mode == "encrypt":
                shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
            # Decrypting
            elif mode == "decrypt":
                shifted = (ord(char) - ord('A') - key) % 26 + ord('A')
            result += chr(shifted)
        else:
            print("Invalid character detected. Please use letters A-Z only.")
            return None
    return result


def caesar_cipher_two_keys(text, key1, key2, mode):
    result = ""
    # Convert text to uppercase and remove spaces
    text = text.upper().replace(" ", "")

    key2 = [ord(char) - ord('A') for char in key2]  # Convert key2 letters to their corresponding shift values
    key_length = len(key2)

    for i, char in enumerate(text):
        if 'A' <= char <= 'Z':
            if mode == "encrypt":
                key_shift = key1 + key2[i % key_length]  # Add key1 and key2 shift
                shifted = (ord(char) - ord('A') + key_shift) % 26 + ord('A')
            elif mode == "decrypt":
                key_shift = key1 + key2[i % key_length]  # Subtract key1 and key2 shift
                shifted = (ord(char) - ord('A') - key_shift) % 26 + ord('A')
            result += chr(shifted)
        else:
            print("Invalid character detected. Please use letters A-Z only.")
            return None
    return result


def main():
    print("Task 1.1: Caesar Cipher with One Key")
    while True:
        operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
        if operation not in ["encrypt", "decrypt"]:
            print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
            continue

        try:
            key = int(input("Enter key (1-25): "))
            if key < 1 or key > 25:
                print("Key must be between 1 and 25. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for the key.")
            continue

        message = input("Enter your message: ")

        if operation == "encrypt":
            result = caesar_cipher(message, key, "encrypt")
            print("Encrypted message:", result)
        else:
            result = caesar_cipher(message, key, "decrypt")
            print("Decrypted message:", result)


def main_two_keys():
    print("\nTask 1.2: Caesar Cipher with Two Keys")
    while True:
        operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
        if operation not in ["encrypt", "decrypt"]:
            print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")
            continue

        try:
            key1 = int(input("Enter key1 (1-25): "))
            if key1 < 1 or key1 > 25:
                print("Key1 must be between 1 and 25. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer for key1.")
            continue

        key2 = input("Enter key2 (minimum 7 letters): ")
        if len(key2) < 7 or not all('A' <= char <= 'Z' for char in key2.upper()):
            print("Key2 must be at least 7 letters from the Latin alphabet. Try again.")
            continue

        message = input("Enter your message: ")

        if operation == "encrypt":
            result = caesar_cipher_two_keys(message, key1, key2.upper(), "encrypt")
            print("Encrypted message:", result)
        else:
            result = caesar_cipher_two_keys(message, key1, key2.upper(), "decrypt")
            print("Decrypted message:", result)


if __name__ == "__main__":
    main()
    main_two_keys()
