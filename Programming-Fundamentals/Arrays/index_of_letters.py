a = 97
word = input()

result = ''
for char in word:
    result += f'{char} -> {ord(char) - a}\n'
print(result)
