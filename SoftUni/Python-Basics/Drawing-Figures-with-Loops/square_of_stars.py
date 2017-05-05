count = int(input())

star = '*'
space = ' '
new_line = '\n'
square = ''
for i in range(1, count + 1):
    square += '{0}{1}'.format(count * (star + space), new_line)

print(square)
