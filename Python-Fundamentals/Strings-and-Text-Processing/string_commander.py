text = input()
length = len(text)
line = input()

result = list(text)
while line != 'end':
    command, params = line.split(' ', 1)
    if command == 'Left':
        left = int(params)
        left %= length
        for i in range(left):
            first = result.pop(0)
            result.insert(length - 1, first)

    elif command == 'Right':
        right = int(params)
        right %= length
        for i in range(right):
            last = result.pop(length - 1)
            result.insert(0, last)

    elif command == 'Insert':
        index, string = filter(None, params.split(' '))
        index = int(index)
        string = list(string)
        result[index:index] = string

    elif command == 'Delete':
        start, end = list(map(int, filter(None, params.split(' '))))
        result = result[:start] + result[end + 1:]

    line = input()

print(''.join([str(c) for c in result]))
