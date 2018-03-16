from random import shuffle

words = input().split(' ')
indices = [i for i in range(len(words))]
shuffle(indices)

result = ''
for i in indices:
    result += f'{words[i]}\n'
print(result)
