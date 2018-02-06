text = input()

count = {}
for letter in text:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

result = ''
for key in count:
    result += f'{key} -> {count[key]}\n'
print(result)
