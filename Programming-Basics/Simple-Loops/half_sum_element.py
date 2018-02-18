import sys

count = int(input())
maximal = -sys.maxsize
total = 0

for number in range(count):
    current = int(input())
    if current > maximal:
        maximal = current
    total += current

sum_of_others = int(abs(total - maximal))
if sum_of_others == maximal:
    print(f'Yes\nSum = {maximal}')
elif sum_of_others != maximal:
    difference = int(abs(sum_of_others - maximal))
    print(f'No\nDiff = {difference}')
