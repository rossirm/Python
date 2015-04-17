__author__ = 'Боян'


def count_vowels_consonants(word):
    vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z",
                  "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]

    letters = {"vowels": 0, "consonants": 0}
    for letter in word:
        if letter in vowels:
            letters["vowels"] += 1
        if letter in consonants:
            letters["consonants"] += 1

    return letters


print(count_vowels_consonants("aaaAcccD"))