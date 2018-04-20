text = input()

chars = ''
for c in text:
    if c not in chars:
        chars += c

result = ''
for char in chars:
    result += f'{char}:'

    ch_index = text.find(char)
    while -1 < ch_index:
        result += f'{ch_index}'
        ch_index = text.find(char, ch_index + 1)
        if -1 < ch_index:
            result += '/'
    result += '\n'

print(result)
