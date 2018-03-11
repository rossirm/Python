numbers = list(map(int, filter(None, input().split(' '))))

numbers.sort()
total = sum(numbers)
average = total / len(numbers)

result = f'Min = {numbers[0]}\n' \
         f'Max = {numbers[len(numbers) - 1]}\n' \
         f'Sum = {total}\n' \
         f'Average = {average:.15g}'
print(result)
