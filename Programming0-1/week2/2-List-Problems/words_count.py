__author__ = 'Боян'

word = input("Enter a word: ")
count = input("Enter the count of the other words: ")
words_count = int(count)

found = 0

counter = 1
while counter <= words_count:
    words = input("Enter a word: ")

    if word in words:
        found += 1

    counter += 1

print("{0} is found {1} time/s".format(word, found))