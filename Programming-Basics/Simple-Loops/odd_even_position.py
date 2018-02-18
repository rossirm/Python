import sys

count = int(input())

odd_sum = 0.0
odd_minimal = sys.maxsize
odd_maximal = -sys.maxsize
even_sum = 0.0
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
    result = f'OddSum={odd_sum:g}, OddMin=No, OddMax=No, ' \
             f'EvenSum={even_sum:g}, EvenMin=No, EvenMax=No'
elif count == 1:
    result = f'OddSum={odd_sum:g}, OddMin={odd_minimal:g}, OddMax={odd_maximal:g}, ' \
             f'EvenSum={even_sum:g}, EvenMin=No, EvenMax=No'
else:
    result = f'OddSum={odd_sum:g}, OddMin={odd_minimal:g}, OddMax={odd_maximal:g}, ' \
             f'EvenSum={even_sum:g}, EvenMin={even_minimal:g}, EvenMax={even_maximal:g}'

print(result)
