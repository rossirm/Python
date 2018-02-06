numbers = list(map(float, input().split(' ')))

count = {}
for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

result = ''
for key in sorted(count):
    result += f'{key} -> {count[key]} times\n'
print(result)
