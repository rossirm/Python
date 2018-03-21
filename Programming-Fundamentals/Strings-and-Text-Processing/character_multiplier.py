first, second = input().split()

common = min(len(first), len(second))
rest = ''
if len(first) > len(second):
    rest = first[common:]
elif len(first) < len(second):
    rest = second[common:]

result = 0
for i in range(common):
    result += ord(first[i]) * ord(second[i])
result += sum([ord(c) for c in rest])
print(result)