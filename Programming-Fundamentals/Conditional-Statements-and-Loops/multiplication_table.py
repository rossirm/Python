number = int(input())

result = ''
for i in range(1, 11):
    result += f'{number} X {i} = {number * i}\n'

print(result)
