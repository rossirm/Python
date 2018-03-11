numbers = list(map(int, filter(None, input().split(' '))))

positives = [x for x in numbers if x >= 0]
positives.reverse()

result = ' '.join([str(i) for i in positives])
print(result if len(positives) > 0 else 'empty')
