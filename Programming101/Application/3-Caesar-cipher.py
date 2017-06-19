__author__ = 'Боян'


def caesar_encrypt(message, n):
    encrypted = ""
    current_char = 0

    while current_char < len(message):
        current_letter = message[current_char]
        is_letter = current_letter.isalpha()

        if is_letter:
            encrypted_letter = encrypt(current_letter, n)
            encrypted += encrypted_letter
        else:
            encrypted += current_letter
        current_char += 1

    return encrypted


def encrypt(letter, num):
        is_lower = letter.islower()
        is_upper = letter.isupper()
        ascii_num = ord(letter)
        caesar = ascii_num + num

        if is_lower:
            while not 97 <= caesar <= 122:
                caesar -= 26
        elif is_upper:
            while not 65 <= caesar <= 90:
                caesar -= 26

        return chr(caesar)


print(caesar_encrypt("abc", 1))
print(caesar_encrypt("ABC", 1))
print(caesar_encrypt("abc", 2))
print(caesar_encrypt("0}x", 7))
print(caesar_encrypt("xyz", 1))