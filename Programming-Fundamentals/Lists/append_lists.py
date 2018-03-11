lists = list(filter(None, input().split('|')))
lists.reverse()

numbers = []
for l in lists:
    filtered = list(filter(None, l.split(' ')))
    for number in filtered:
        numbers.append(number)

result = ' '.join([str(number) for number in numbers])
print(result)
