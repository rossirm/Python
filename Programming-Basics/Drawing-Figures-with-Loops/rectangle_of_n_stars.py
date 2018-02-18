count = int(input())

star = '*'
new_line = '\n'

rectangle = ''
for i in range(count):
    rectangle += f'{count * star}{new_line}'

print(rectangle)
