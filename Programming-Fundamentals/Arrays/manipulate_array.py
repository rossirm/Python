strings = input().split(' ')
count = int(input())

for c in range(count):
    command, *params = input().split(' ')
    if command == 'Reverse':
        strings.reverse()
    elif command == 'Distinct':
        unique = []
        for s in strings:
            if s not in unique:
                unique.append(s)
        strings = unique
    elif command == 'Replace':
        index, value = params
        strings[int(index)] = value

print(', '.join(strings))
