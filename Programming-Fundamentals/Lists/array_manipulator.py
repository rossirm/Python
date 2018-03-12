numbers = list(map(int, input().split(' ')))

line = input()
while line != 'print':
    length = len(numbers)
    command, *params = line.split(' ')

    if command == 'add':
        index, element = params
        numbers.insert(int(index), int(element))
    elif command == 'addMany':
        index, *elements = params
        numbers = numbers[:int(index)] + list(map(int, elements)) + numbers[int(index):]
    elif command == 'contains':
        element = int(params[0])
        if element in numbers:
            print(numbers.index(element))
        else:
            print(-1)
    elif command == 'remove':
        index = int(params[0])
        del numbers[index]
    elif command == 'shift':
        positions = int(params[0])
        shifted = [None] * length
        for i in range(length):
            position = (i + positions) % length
            shifted[i] = numbers[position]
        numbers = shifted
    elif command == 'sumPairs':
        summed = []
        for i in range(0, length - 1, 2):
            summed.append(numbers[i] + numbers[i + 1])
        if length % 2 != 0:
            summed.append(numbers[length - 1])
        numbers = summed

    line = input()

print(numbers)
