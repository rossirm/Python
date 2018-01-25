numbers = [int(number) for number in input().split()]
positives = [x for x in numbers if x >= 0]

result = ''
if len(positives) == 0:
    result = 'empty'
else:
    positives = positives[::-1]
    result = ' '.join([str(number) for number in positives])
print(result)
