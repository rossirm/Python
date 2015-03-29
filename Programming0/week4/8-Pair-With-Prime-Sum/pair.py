__author__ = 'Боян'
from math import sqrt


def is_prime(number):
    prime_checker = 2
    is_prime_num = True

    while prime_checker <= sqrt(number):
        if number % prime_checker == 0:
            is_prime_num = False
            break
        prime_checker += 1

    return is_prime_num


def prime_pair(numbers):
    has_prime_pair = False

    for x in numbers:
        for y in numbers:
            if is_prime(x + y):
                has_prime_pair = True

    return has_prime_pair


print(prime_pair([1, 2, 3, 4, 5]))