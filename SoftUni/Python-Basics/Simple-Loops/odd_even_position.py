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
        if current < even_minimal:
            even_minimal = current
        if current > even_maximal:
            even_maximal = current
    else:
        odd_sum += current
        if current < odd_minimal:
            odd_minimal = current
        if current > odd_maximal:
            odd_maximal = current

result = ''
if count == 0:
    result = 'OddSum={0:g}, OddMin=No, OddMax=No, ' \
             'EvenSum={1:g}, EvenMin=No, EvenMax=No'.format(odd_sum, even_sum)
elif count == 1:
    result = 'OddSum={0:g}, OddMin={1:g}, OddMax={2:g}, ' \
             'EvenSum={3:g}, EvenMin=No, EvenMax=No'.format(round(odd_sum, 2),
                                                            round(odd_minimal, 2),
                                                            round(odd_maximal, 2),
                                                            round(even_sum, 2))
else:
    result = 'OddSum={0:g}, OddMin={1:g}, OddMax={2:g}, ' \
             'EvenSum={3:g}, EvenMin={4:g}, EvenMax={5:g}'.format(round(odd_sum, 2),
                                                                  round(odd_minimal, 2),
                                                                  round(odd_maximal, 2),
                                                                  round(even_sum, 2),
                                                                  round(even_minimal, 2),
                                                                  round(even_maximal, 2))

print(result)
