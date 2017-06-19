# Напишете програма, която въвежда цяло число n и отпечатва таблица (матрица) от числа

number = int(input())

mid = (number + 1) // 2
table = ''
for row in range(number):
    for col in range(number):
        current = row + col + 1
        if current >= number:
            table += '{} '.format(number * 2 - current)
        else:
            table += '{} '.format(current)
    table += '\n'

print(table)
