numbers = [int(number) for number in input().split()]
positives = [x for x in numbers if x >= 0]

result = ''
if not positives:
    result = 'empty'
else:
    result = ' '.join([str(number) for number in positives[::-1]])
print(result)
