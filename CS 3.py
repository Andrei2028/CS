def create_playfair_matrix(key):
    key = key.replace("J", "I").upper()
    unique_key = ""
    for char in key:
        if char not in unique_key and char.isalpha():
            unique_key += char
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in unique_key:
            unique_key += char
    matrix = [unique_key[i:i + 5] for i in range(0, len(unique_key), 5)]
    return matrix


def format_message(message):
    message = message.upper().replace("J", "I")
    formatted = ""
    i = 0
    while i < len(message):
        char = message[i]
        if char.isalpha():
            formatted += char
            if i + 1 < len(message) and message[i] == message[i + 1]:
                formatted += 'X'
            i += 1
        else:
            i += 1
    if len(formatted) % 2 != 0:
        formatted += 'X'
    return formatted


def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None


def playfair_encrypt(message, key):
    matrix = create_playfair_matrix(key)
    formatted_message = format_message(message)
    ciphertext = ""
    for i in range(0, len(formatted_message), 2):
        first_char = formatted_message[i]
        second_char = formatted_message[i + 1]
        row1, col1 = find_position(first_char, matrix)
        row2, col2 = find_position(second_char, matrix)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    formatted_ciphertext = ciphertext.upper()
    plaintext = ""
    for i in range(0, len(formatted_ciphertext), 2):
        first_char = formatted_ciphertext[i]
        second_char = formatted_ciphertext[i + 1]
        row1, col1 = find_position(first_char, matrix)
        row2, col2 = find_position(second_char, matrix)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext


def main():
    operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
    key = input("Enter the key (minimum 7 characters): ").strip()
    if len(key) < 7:
        print("Key must be at least 7 characters long.")
        return
    if any(c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in key):
        print("Key must only contain characters from A-Z.")
        return

    if operation == "encrypt":
        message = input("Enter the message to encrypt: ")
        ciphertext = playfair_encrypt(message, key)
        print("Encrypted message:", ciphertext)
    elif operation == "decrypt":
        ciphertext = input("Enter the ciphertext to decrypt: ")
        plaintext = playfair_decrypt(ciphertext, key)
        print("Decrypted message:", plaintext)
    else:
        print("Invalid operation. Please choose either 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
