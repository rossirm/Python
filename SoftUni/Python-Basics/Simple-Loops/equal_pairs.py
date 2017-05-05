import math

count = int(input())
first = float(input())
second = float(input())
total = first + second
max_difference = 0

for number in range(1, count):
    first = float(input())
    second = float(input())

    current_total = first + second
    current_difference = math.fabs(current_total - total)
    if current_difference > max_difference:
        max_difference = current_difference
    total = current_total

result = ''
if max_difference == 0:
    result = 'Yes, value={0:g}'.format(total)
else:
    result = 'No, maxdiff={0:g}'.format(max_difference)

print(result)
