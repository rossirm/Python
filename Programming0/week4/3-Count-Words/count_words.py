__author__ = 'Боян'


def count_words(words):
    words_found = {}

    for word in words:
        if word in words_found:
            words_found[word] += 1
        else:
            words_found[word] = 1

    return words_found


print(count_words(["words", "are", "meaningful", "words", "words", "are"]))