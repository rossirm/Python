# Дадени са 2*n числа.
# Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност
# или печата максималната разлика между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value=…" + стойността.
# В противен случай отпечатайте "No, maxdiff=…" + максималната разлика.
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
