numbers = list(map(float, input().split(' ')))

count = {}
for number in numbers:
    if number not in count:
        count[number] = 0

    count[number] += 1

result = ''
for number, times in sorted(count.items()):
    result += f'{number} -> {times} times\n'

print(result)
