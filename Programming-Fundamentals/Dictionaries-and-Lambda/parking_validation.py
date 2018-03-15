def validate_plate(p):
    return len(p) == 8 and p[:2].isupper() and p[2:6].isdigit() and p[-2:].isupper()


parking = {}
result = ''
count = int(input())
for i in range(count):
    line = input()
    command, *params = line.split(' ')
    if command == 'register':
        name, plate = params
        if name in parking:
            result += f'ERROR: already registered with plate number {parking[name]}\n'
        elif not validate_plate(plate):
            result += f'ERROR: invalid license plate {plate}\n'
        elif plate in parking.values():
            result += f'ERROR: license plate {plate} is busy\n'
        else:
            result += f'{name} registered {plate} successfully\n'
            parking[name] = plate
    elif command == 'unregister':
        name = params[0]
        if name not in parking:
            result += f'ERROR: user {name} not found\n'
        else:
            result += f'user {name} unregistered successfully\n'
            del parking[name]

for name, plate in parking.items():
    result += f'{name} => {plate}\n'
print(result)
