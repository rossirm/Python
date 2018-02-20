number = int(input())
start = int(input())
end = start + 1 if start > 10 else 11

result = ''
for i in range(start, end):
    result += f'{number} X {i} = {number * i}\n'

print(result)
