numbers = [int(number) for number in input().split()]
multiplier = int(input())

multiplied = []
for i in range(len(numbers)):
    multiplied.append(numbers[i] * multiplier)

result = ' '.join([str(number) for number in multiplied])
print(result)
