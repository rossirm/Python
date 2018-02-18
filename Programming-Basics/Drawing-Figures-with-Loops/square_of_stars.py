count = int(input())

star = '* '
new_line = '\n'

square = ''
for i in range(count):
    square += f'{count * star}{new_line}'

print(square)
