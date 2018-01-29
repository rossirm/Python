start = int(input())
end = int(input())
if start > end:
    end = start + end
    start = end - start
    end = end - start

result = ''
for i in range(start, end + 1):
    result += f'{i}\n'
print(result)
