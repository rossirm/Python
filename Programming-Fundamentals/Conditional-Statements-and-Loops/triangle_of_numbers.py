count = int(input())

triangle = ''
for i in range(1, count + 1):
    triangle += f'{i} ' * i + '\n'
print(triangle)
