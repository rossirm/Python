text = input()

letters = {}
for letter in text:
    if letter not in letters:
        letters[letter] = 0

    letters[letter] += 1

result = ''
for letter, times in letters.items():
    result += f'{letter} -> {times}\n'

print(result)
