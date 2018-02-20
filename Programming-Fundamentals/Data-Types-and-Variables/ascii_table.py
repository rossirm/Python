start = int(input())
end = int(input()) + 1

result = ''
for i in range(start, end):
    result += f'{chr(i)} '
print(result)
