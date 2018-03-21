text = input()

unicode = ''
for c in text:
    unicode += f'\\u{ord(c):04x}'
print(unicode)
