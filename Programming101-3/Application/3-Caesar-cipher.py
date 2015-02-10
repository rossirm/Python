__author__ = 'Боян'


def caesar_encrypt(str, n):
    encrypted = ""
    for char in str:
        current = ord(char)
        enc = (current + n)

        encrypted = str(enc) + encrypted
        # print(chr(current + 99))
    return encrypted


caesar_encrypt("azy", 3)