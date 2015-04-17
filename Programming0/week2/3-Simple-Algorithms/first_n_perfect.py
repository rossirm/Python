__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

perfect_counter = 0
number = 1

while perfect_counter < num:
    divisors_sum = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            divisors_sum += divisor
        divisor += 1

    if number == divisors_sum:
        perfect_counter += 1
        print(number)

    number += 1