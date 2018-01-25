from math import sqrt

numbers = [int(number) for number in input().split(' ')]
squares = [x for x in numbers if sqrt(x) == int(sqrt(x))]
squares.sort(reverse=True)
result = ' '.join([str(number) for number in squares])
print(result)
