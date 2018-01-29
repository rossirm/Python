count = int(input())
total = 0

result = ''
for i in range(1, count * 2, 2):
    result += f'{i}\n'
    total += i
result += f'Sum: {total}'

print(result)
