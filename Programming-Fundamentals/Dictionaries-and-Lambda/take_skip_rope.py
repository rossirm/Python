text = input()
digits = ''
letters = ''

for c in text:
    if c.isdigit():
        digits += c
    else:
        letters += c
take = []
skip = []
for d in range(len(digits)):
    if d % 2 == 0:
        take.append(int(digits[d]))
    else:
        skip.append(int(digits[d]))

result = ''
skipped = 0
for i in range(len(take)):
    result += letters[skipped:(skipped + take[i])]
    skipped += skip[i]+ take[i]
print(result)
