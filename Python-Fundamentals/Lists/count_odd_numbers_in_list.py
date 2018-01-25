numbers = [int(number) for number in input().split()]
odds = [x for x in numbers if x % 2 != 0]

print(len(odds))
