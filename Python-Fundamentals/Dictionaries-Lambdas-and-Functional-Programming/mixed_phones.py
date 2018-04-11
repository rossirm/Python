phones = {}

line = input()
while line != 'Over':
    name, number = line.split(' : ')

    if number.isdigit():
        phones[name] = number
    else:
        phones[number] = name

    line = input()

result = ''
for entry, phone in sorted(phones.items()):
    result += f'{entry} -> {phone}\n'

print(result)
