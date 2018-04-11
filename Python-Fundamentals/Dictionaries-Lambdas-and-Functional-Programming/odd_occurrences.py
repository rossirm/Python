text = input().lower().split(' ')

words = {}
for word in text:
    if word not in words:
        words[word] = 0

    words[word] += 1

result = ', '.join([str(w) for w in words if words[w] % 2 != 0])

print(result)
