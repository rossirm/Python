start = ord(input())
end = ord(input())
skip = ord(input())

result = ''
for a in range(start, end + 1):
    for b in range(start, end + 1):
        for c in range(start, end + 1):
            if a != skip and b != skip and c != skip:
                result += f'{chr(a)}{chr(b)}{chr(c)} '
print(result)
