text = input().lower().split(' ')

words = {}
for word in text:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

result = ', '.join([w for w in words if words[w] % 2 != 0])
print(result)
