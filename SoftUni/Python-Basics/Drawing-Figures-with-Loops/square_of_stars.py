# Напишете програма, която чете от конзолата число n и чертае квадрат от n * n звездички.
# Разликата с предходната задача е, че между всеки две звездички има по един интервал.

count = int(input())

star = '*'
space = ' '
new_line = '\n'

square = ''
for i in range(count):
    square += '{0}{1}'.format(count * (star + space), new_line)

print(square)
