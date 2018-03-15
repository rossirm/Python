count = int(input())
numbers = []
for n in range(count):
    numbers.append(int(input()))

numbers.sort()
total = sum(numbers)
average = total / len(numbers)

result = f'Sum = {total}\n' \
         f'Min = {numbers[0]}\n' \
         f'Max = {numbers[len(numbers) - 1]}\n' \
         f'Average = {average:.15g}'
print(result)
