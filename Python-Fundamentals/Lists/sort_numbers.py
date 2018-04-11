numbers = [int(number) for number in input().split(' ')]

numbers.sort()
result = ' <= '.join([str(number) for number in numbers])

print(result)
