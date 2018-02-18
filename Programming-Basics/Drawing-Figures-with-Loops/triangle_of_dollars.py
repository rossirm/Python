count = int(input())

dollar = '$ '
new_line = '\n'

triangle = ''
for i in range(1, count + 1):
    triangle += f'{i * dollar}{new_line}'

print(triangle)
