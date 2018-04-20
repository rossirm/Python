text = input()
command = input()

total = 0
if command == 'UPPERCASE':
    total = sum([ord(l) for l in text if l.isupper()])
elif command == 'LOWERCASE':
    total = sum([ord(l) for l in text if l.islower()])
else:
    total = sum([ord(l) for l in text if not l.isalpha()])

print(f'The total sum is: {total}')
