def manipulate(storage):
    line = input()
    while line != 'END':
        command, *params = filter(None, line.split(' '))
        if command == 'Reverse':
            storage.reverse()
        elif command == 'Distinct':
            unique = []
            for s in storage:
                if s not in unique:
                    unique.append(s)
                    storage = unique
        elif command == 'Replace':
            index = int(params[0])
            value = params[1]
            if 0 <= index < len(storage):
                storage[index] = value
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')

        line = input()
    return storage


strings = input().split(' ')
result = manipulate(strings)
print(', '.join(result))
