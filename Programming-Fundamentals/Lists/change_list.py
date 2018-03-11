integers = list(map(int, filter(None, input().split(' '))))

line = input()
while line != 'Odd' and line != 'Even':
    command, *params = line.split(' ')
    if command == 'Delete':
        value = int(params[0])
        integers = [x for x in integers if int(x) != value]
    elif command == 'Insert':
        value = int(params[0])
        index = int(params[1])
        integers.insert(index, value)

    line = input()

result = ''
if line == 'Even':
    result = ' '.join([str(x) for x in integers if x % 2 == 0])
elif line == 'Odd':
    result = ' '.join([str(x) for x in integers if x % 2 != 0])

print(result)
