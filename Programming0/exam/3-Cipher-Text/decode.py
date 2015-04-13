__author__ = 'Боян'


def decode_word(encrypted_word, cipher):
    decrypted_word = ""

    for char in range(0, len(encrypted_word)):
        for code in cipher:
            if cipher[code] == encrypted_word[char]:
                decrypted_word += str(code)

    return decrypted_word


print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
# 'python'
print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
# 'omg'
print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
# 'programming'
print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))
# 'aaaaaaaaaaaaaaaaaaaaaaaaaaa'