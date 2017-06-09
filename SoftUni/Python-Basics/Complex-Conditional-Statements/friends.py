first = input().lower()
second = input().lower()
result = ''

if (first == 'out') ^ (second == 'out'):
    result = 'Go out!'
else:
    result = 'Stay at home!'

print(result)
