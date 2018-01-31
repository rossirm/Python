count = int(input())
start = ord('a')
end = start + count

result = ''
for a in range(start, end):
    for b in range(start, end):
        for c in range(start, end):
            result += f'{chr(a)}{chr(b)}{chr(c)}\n'
print(result)
