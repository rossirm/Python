# Да се напише програма, която въвежда n цели числа
# и проверява дали сумата от числата на четни позиции
# е равна на сумата на числата на нечетни позиции.
# При равенство да се отпечата "Yes" + сумата
# иначе да се отпечата "No" + разликата.
# Разликата се изчислява по абсолютна стойност.
import math

count = int(input())

odd_sum = 0
even_sum = 0
for number in range(count):
    if number % 2 == 0:
        even_sum += int(input())
    elif number % 2 != 0:
        odd_sum += int(input())

difference = int(math.fabs(odd_sum - even_sum))
if difference == 0:
    print('Yes\nSum = {}'.format(even_sum))
else:
    print('No\nDiff = {}'.format(difference))
