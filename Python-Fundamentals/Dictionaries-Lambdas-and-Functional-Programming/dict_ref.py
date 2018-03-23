dictionary = {}

line = input()
while line != 'end':
    name, value = line.split(' = ')

    if value.isdigit():
        dictionary[name] = int(value)
    else:
        if value in dictionary:
            dictionary[name] = dictionary[value]

    line = input()

result = ''
for entry in dictionary:
    result += f'{entry} === {dictionary[entry]}\n'
print(result)
