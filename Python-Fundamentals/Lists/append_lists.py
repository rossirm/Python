lists = list(filter(None, input().split('|')))
lists.reverse()

numbers = []
for l in lists:
    numbers.extend(list(filter(None, l.split(' '))))

result = ' '.join([str(number) for number in numbers])

print(result)
