# Напишете програма, която чете n числа и пресмята сумата, минимума и максимума на числата
# на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте “No”.
import sys

count = int(input())

odd_sum = 0
odd_minimal = sys.maxsize
odd_maximal = -sys.maxsize
even_sum = 0
even_minimal = sys.maxsize
even_maximal = -sys.maxsize

for number in range(count):
    current = float(input())
    if number % 2 != 0:
        even_sum += current
        if current <= even_minimal:
            even_minimal = current
        if current >= even_maximal:
            even_maximal = current
    else:
        odd_sum += current
        if current <= odd_minimal:
            odd_minimal = current
        if current >= odd_maximal:
            odd_maximal = current

result = ''
if count == 0:
    result = 'OddSum={0:.1f}, OddMin=No, OddMax=No, ' \
             'EvenSum={1:.1f}, EvenMin=No, EvenMax=No'.format(odd_sum, even_sum)
elif count == 1:
    result = 'OddSum={0:.1f}, OddMin={1:.1f}, OddMax={2:.1f}, ' \
             'EvenSum={3:.1f}, EvenMin=No, EvenMax=No'.format(round(odd_sum, 2),
                                                              round(odd_minimal, 2),
                                                              round(odd_maximal, 2),
                                                              round(even_sum, 2))
else:
    result = 'OddSum={0:.1f}, OddMin={1:.1f}, OddMax={2:.1f}, ' \
             'EvenSum={3:.1f}, EvenMin={4:.1f}, EvenMax={5:.1f}'.format(round(odd_sum, 2),
                                                                        round(odd_minimal, 2),
                                                                        round(odd_maximal, 2),
                                                                        round(even_sum, 2),
                                                                        round(even_minimal, 2),
                                                                        round(even_maximal, 2))

print(result)
