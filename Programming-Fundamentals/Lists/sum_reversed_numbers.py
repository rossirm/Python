numbers = input().split(' ')

total = sum([int(x[::-1]) for x in numbers])
print(total)
