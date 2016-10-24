__author__ = 'Боян'
from math import sqrt

num = input("Enter a number")
n = int(num)

prime_digits = []
for number in range(n - 2, n + 2 + 1):
    prime_checker = 2
    is_prime = True

    while prime_checker <= sqrt(number):
        if number % prime_checker == 0:
            is_prime = False
            break
        prime_checker += 1
    if is_prime:
        prime_digits += number

n_is_prime = n in prime_digits
has_two_twins = n - 2 in prime_digits and n + 2 in prime_digits
has_lesser_twin = n - 2 in prime_digits
has_bigger_twin = n + 2 in prime_digits

if n_is_prime:
    print("{0} is prime".format(num), end="")
    if has_two_twins:
        print(" and has 2 twins: {0} {1}".format(n - 2, n + 2))
    elif has_lesser_twin:
        print(" and has 1 lesser twin: {0}".format(n - 2))
    elif has_bigger_twin:
        print(" and has 1 bigger twin: {0}".format(n + 2))
    else:
        print(" and has no twins")

elif not n_is_prime:
    print("{0} is not prime".format(num), end="")
    if has_two_twins:
        print(" and has 2 twins: {0} {1}".format(n - 2, n + 2))
    elif has_lesser_twin:
        print(" and has 1 lesser twin: {0}".format(n - 2))
    elif has_bigger_twin:
        print(" and has 1 bigger twin: {0}".format(n + 2))
    else:
        print(" and has no twins")