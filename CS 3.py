import string


def generate_key_matrix(key):
    key = ''.join(sorted(set(key), key=key.index))
    key += ''.join([ch for ch in string.ascii_uppercase if ch not in key])
    return [key[i:i + 5] for i in range(0, 25, 5)]


def preprocess_message(message):
    message = ''.join([ch for ch in message.upper() if ch in string.ascii_uppercase])
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
        i += 2
    if len(message) % 2 != 0:
        message += 'X'
    return message


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return (i, row.index(char))
    return None


def encrypt_decrypt(message, key, mode):
    matrix = generate_key_matrix(key)
    message = preprocess_message(message)
    result = ''

    for i in range(0, len(message), 2):
        pos1 = find_position(matrix, message[i])
        pos2 = find_position(matrix, message[i + 1])

        if pos1[0] == pos2[0]:
            if mode == 'encrypt':
                result += matrix[pos1[0]][(pos1[1] + 1) % 5]
                result += matrix[pos2[0]][(pos2[1] + 1) % 5]
            else:
                result += matrix[pos1[0]][(pos1[1] - 1) % 5]
                result += matrix[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:
            if mode == 'encrypt':
                result += matrix[(pos1[0] + 1) % 5][pos1[1]]
                result += matrix[(pos2[0] + 1) % 5][pos2[1]]
            else:
                result += matrix[(pos1[0] - 1) % 5][pos1[1]]
                result += matrix[(pos2[0] - 1) % 5][pos2[1]]
        else:
            result += matrix[pos1[0]][pos2[1]]
            result += matrix[pos2[0]][pos1[1]]

    return result


def playfair_cipher():
    key = input("Introduceți cheia (minim 7 caractere): ")
    if len(key) < 7:
        print("Cheia trebuie să aibă cel puțin 7 caractere.")
        return

    operation = input("Alegeți operația (criptare/decriptare): ").lower()
    if operation not in ['criptare', 'decriptare']:
        print("Operația trebuie să fie 'criptare' sau 'decriptare'.")
        return

    message = input("Introduceți mesajul/criptograma: ")
    invalid_chars = [ch for ch in message if ch not in string.ascii_letters]
    if invalid_chars:
        print(f"Valori incorecte introduse: {', '.join(invalid_chars)}. Permise: 'A'-'Z', 'a'-'z'.")
        return

    result = encrypt_decrypt(message, key, operation)
    print(f"Rezultatul: {result}")


playfair_cipher()
