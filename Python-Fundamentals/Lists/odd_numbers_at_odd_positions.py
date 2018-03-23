numbers = [int(number) for number in input().split()]

result = ''
for (index, number) in enumerate(numbers):
    if index % 2 != 0 and number % 2 != 0:
        result += f'Index {index} -> {number}\n'

print(result)
