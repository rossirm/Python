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

# n = input("Enter a number")
# nth_count = int(n)
# nth_counter = 1
# p = 2
# while nth_counter <= nth_count:
# is_prime = True
#     is_mersenne=False
#     checker = 2
#
#     while checker < sqrt(p):
#         if p % checker == 0:
#             is_prime = False
#             break
#
#         m = p - 1
#         is_mersenne = False
#
#         while m > 2:
#             m /= 2
#         if m % 2 == 0:
#             is_mersenne = True
#         else:
#             is_mersenne = False
#     if is_prime and is_mersenne:
#
#         perfect_n = (2 ** (p - 1)) * ((2 ** p) - 1)
#         print(perfect_n)
#         nth_counter += 1
#     p += 1
