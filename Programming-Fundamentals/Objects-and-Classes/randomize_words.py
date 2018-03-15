import random

words = input().split(' ')
l = len(words)
result = ''
while words:
    r_index = random.randint(0, len(words) - 1)
    result += f'{words[r_index]}\n'
    words.pop(r_index)
print(result)
