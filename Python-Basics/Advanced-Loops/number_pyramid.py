# Напишете програма, която въвежда цяло число n и отпечатва пирамида от числа

number = int(input())

current = 1
pyramid = ''
for row in range(1, number + 1):
    for col in range(row):
        pyramid += ('{0} '.format(current))
        current += 1
        if current > number:
            break
    if current > number:
        break
    pyramid += '\n'

print(pyramid)
