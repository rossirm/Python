# Да се напише програма, която въвежда 2*n цели числа
# и проверява дали сумата на първите n числа (лява сума)
# е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes" + сумата; иначе печата "No" + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).
import math

count = int(input())

left_sum = 0
right_sum = 0
for l in range(count):
    left_sum += int(input())
for r in range(count):
    right_sum += int(input())

difference = int(math.fabs(left_sum - right_sum))
if difference == 0:
    print('Yes, sum = {}'.format(right_sum))
else:
    print('No, diff = {}'.format(difference))
