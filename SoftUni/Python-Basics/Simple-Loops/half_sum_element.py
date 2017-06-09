# Да се напише програма, която въвежда n цели числа
# и проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# Ако има такъв елемент, печата "Yes" + неговата стойност
# иначе печата "No" + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност).
import sys
import math

count = int(input())
maximal = -sys.maxsize
total = 0

for number in range(count):
    current = int(input())
    if current > maximal:
        maximal = current
    total += current
    
sum_of_others = int(math.fabs(total - maximal))
if sum_of_others == maximal:
    print('Yes\nSum = {}'.format(maximal))
elif sum_of_others != maximal:
    difference = int(math.fabs(sum_of_others - maximal))
    print('No\nDiff = {}'.format(difference))
