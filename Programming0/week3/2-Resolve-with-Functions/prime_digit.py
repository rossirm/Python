__author__ = 'Боян'
from math import sqrt


def to_digits(number):
    digits = []

    for digit in str(number):
        digits += [int(digit)]
    return digits


def is_prime(number):
    prime_checker = 2
    is_prime_num = True

    while prime_checker <= sqrt(number):
        if number % prime_checker == 0:
            is_prime_num = False
            break
        prime_checker += 1

    return is_prime_num


def has_prime_digits(number):
    prime_digits = []
    digits = to_digits(number)

    for digit in digits:
        if is_prime(digit):
            prime_digits += [digit]

    if len(prime_digits) > 0:
        return prime_digits
    else:
        return 0


n = input("Enter a number")
result = has_prime_digits(int(n))
print("{0} has {1} prime digits".format(int(n), result))