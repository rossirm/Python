__author__ = 'Боян'

word = input("Enter a word: ")
wordcnt = input("Enter the count of the other words: ")
words_count = int(wordcnt)

found = 0

counter = 1
while counter <= words_count:
    words = input("Enter a word: ")
    if word in words:
        found += 1
    counter += 1

print("{0} is found {1} time/s".format(word, found))