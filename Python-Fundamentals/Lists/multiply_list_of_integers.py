numbers = [int(number) for number in input().split()]
multiplier = int(input())

multiplied = [n * multiplier for n in numbers]

result = ' '.join([str(number) for number in multiplied])
print(result)
