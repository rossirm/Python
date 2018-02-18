number = int(input())

mid = (number + 1) // 2
table = ''
for row in range(number):
    for col in range(number):
        current = row + col + 1
        if current >= number:
            table += f'{number * 2 - current} '
        else:
            table += f'{current} '
    table += '\n'

print(table)
