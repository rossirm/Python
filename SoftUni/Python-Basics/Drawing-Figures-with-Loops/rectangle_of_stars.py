star = '* '
new_line = '\n'
rectangle = ''
for i in range(1, 11):
    rectangle += '{0}{1}'.format(10 * star, new_line)

print(rectangle)
