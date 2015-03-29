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

num = input("Enter a number")
n = int(num)

if is_prime(n):
    print("{} is prime".format(num), end="")
    if is_prime(n-2) and is_prime(n+2):
        print(" and has 2 twins: {0} {1}".format(n - 2, n + 2))
    elif is_prime(n-2):
        print(" and has 1 lesser twin: {0}".format(n - 2))
    elif is_prime(n+2):
        print(" and has 1 bigger twin: {0}".format(n + 2))
    else:
        print(" and has no twins")
elif not is_prime(n):
    print("{} is not prime".format(num), end="")
    if is_prime(n-2) and is_prime(n+2):
        print(" and has 2 twins: {0} {1}".format(n - 2, n + 2))
    elif is_prime(n-2):
        print(" and has 1 lesser twin: {0}".format(n - 2))
    elif is_prime(n+2):
        print(" and has 1 bigger twin: {0}".format(n + 2))
    else:
        print(" and has no twins")