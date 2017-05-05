import math

count = int(input())

odd_sum = 0
even_sum = 0
for number in range(count):
    if number % 2 == 0:
        even_sum += int(input())
    elif number % 2 != 0:
        odd_sum += int(input())

difference = math.fabs(odd_sum - even_sum)
if difference == 0:
    print('yes sum {}'.format(even_sum))
else:
    print('no diff {}'.format(difference))
