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
for entry in sorted(phones):
    result += f'{entry} -> {phones[entry]}\n'
print(result)
