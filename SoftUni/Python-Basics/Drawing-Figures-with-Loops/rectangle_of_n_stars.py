count = int(input())

star = '*'
new_line = '\n'
rectangle = ''
for i in range(1, count + 1):
    rectangle += '{0}{1}'.format(count * star, new_line)

print(rectangle)
