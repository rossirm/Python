phone_book = {}
result = ''

line = input()
while line != 'END':
    command, *params = line.split(' ')

    if command == 'A':
        name, phone = params[0], params[1]
        phone_book[name] = phone
    elif command == 'S':
        name = params[0]
        if name in phone_book:
            result += f'{name} -> {phone_book[name]}\n'
        else:
            result += f'Contact {name} does not exist.\n'

    line = input()
print(result)
