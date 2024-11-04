def caesar_cipher(text, key1, key2=None, mode='encrypt'):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper().replace(" ", "")
    if key1 < 1 or key1 > 25 or (key2 and (len(key2) < 7 or not all(c in alphabet for c in key2.upper()))):
        return "Invalid key(s)"

    result = ""
    for i, char in enumerate(text):
        if char in alphabet:
            index = alphabet.index(char)
            shift = key1 if key2 is None or i % 2 == 0 else alphabet.index(key2[i % len(key2)].upper())
            shift = shift if mode == 'encrypt' else -shift
            result += alphabet[(index + shift) % 26]

    return result


# Get user input
mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
text = input("Enter the text: ").strip()
key1 = int(input("Enter key 1 (1-25): "))

# Check if the user wants to use a second key
use_key2 = input("Do you want to use a second key? (yes/no): ").strip().lower()
key2 = None
if use_key2 == "yes":
    key2 = input("Enter key 2 (at least 7 letters, Latin alphabet only): ").strip()

# Execute the cipher
result = caesar_cipher(text, key1, key2, mode)
print("Result:", result)
