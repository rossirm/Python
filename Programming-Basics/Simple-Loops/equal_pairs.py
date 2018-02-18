count = int(input())
first = float(input())
second = float(input())
total = first + second
max_difference = 0

for number in range(1, count):
    first = float(input())
    second = float(input())

    current_total = first + second
    current_difference = abs(current_total - total)
    if current_difference > max_difference:
        max_difference = current_difference
    total = current_total

result = ''
if max_difference == 0:
    result = f'Yes, value={total:g}'
else:
    result = f'No, maxdiff={max_difference:g}'

print(result)
