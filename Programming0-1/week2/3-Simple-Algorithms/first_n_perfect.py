__author__ = 'Боян'
from math import sqrt

# n = input("Enter a number")
# num = int(n)
# perfect_counter = 0
# number = 1
# while perfect_counter < num:
#
# divisors_sum = 0
# divisor = 1
# while divisor < number:
# if number % divisor == 0:
#             divisors_sum += divisor
#         divisor += 1
#
#     if number == divisors_sum:
#         perfect_counter += 1
#         print(number)f
#     number += 1


# n = input("Enter a number")
# nth_count = int(n)
#
# nth_counter = 1
# p = 2
# while nth_counter <= nth_count:
#     is_prime = True
#     checker = 2
#     while checker < sqrt(p):
#         if p % checker == 0:
#             is_prime = False
#             break
#
#     if is_prime:
#         perfect_n = (2 ** (p - 1)) * ((2 ** p) - 1)
#         print(perfect_n)
#         nth_counter += 1
#
#     p += 1


n = input("Enter n: ")
n = int(n)

start = 6

while True:

    divisors_sum = 0
    divisor = 1

    while divisor < start:
        if start % divisor == 0:
            divisors_sum += divisor

        divisor += 1

    if divisors_sum == start:
        print(start)
        n = n - 1

    if n == 0:
        break

    start += 1