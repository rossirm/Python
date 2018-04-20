line = input()

length = 0
chars = {}

while line != 'end':
    letter, i = line.split(':', 1)
    indices = [int(i) for i in i.split('/')]
    length += len(indices)
    chars[letter] = indices

    line = input()

word = [''] * length
for char, index in chars.items():
    for i in index:
        word[i] = char

print(''.join([str(c) for c in word]))
