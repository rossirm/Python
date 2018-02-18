number = int(input())

current = 1
pyramid = ''
for row in range(1, number + 1):
    for col in range(row):
        pyramid += f'{current} '
        current += 1
        if current > number:
            break
    if current > number:
        break
    pyramid += '\n'

print(pyramid)
