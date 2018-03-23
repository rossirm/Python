words = input().split(', ')
text = input()

filtered = text
for word in words:
    filtered = filtered.replace(word, '*' * len(word))
print(filtered)
