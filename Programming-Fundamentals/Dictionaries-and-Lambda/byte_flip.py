digits = input()
filtered = []
for d in digits.split(' '):
    if len(d) == 2:
        if d.isdigit():
            filtered.append(int(d[::-1], 16))
        else:
            filtered.append(int(d, 16))

hexes = ''.join(reversed([chr(d) for d in filtered]))
print(hexes.encode('utf-8'))
