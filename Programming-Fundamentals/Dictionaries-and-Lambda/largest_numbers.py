numbers = list(map(float, input().split(' ')))
numbers.sort(reverse=True)
count = 3 if len(numbers) >= 3 else len(numbers)
print(' '.join([str(x) for x in numbers[:count]]))
