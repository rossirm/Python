line = input()

while line != 'end':
    longest = -1

    for c in range(len(line) // 2, 0, -1):

        if line[:c] == line[len(line) - c:] and c * 2 < len(line):
            if c > longest:
                longest = c
    try:
        middle = line[longest:len(line) - longest]
        left = line[:longest]
        right= line[len(line) - longest]
        if left == right:
            print(f'{middle}{right}{middle}')
    except IndexError:
        continue
    line = input()
