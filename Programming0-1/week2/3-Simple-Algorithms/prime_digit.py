__author__ = 'Боян'
from math import sqrt

n = input("Enter a number")
# getting the digits of the number
digits = []
for d in n:
    digits += [int(d)]

# getting list of all prime digits
prime_digits = []
for num in range(1, 11):
    prime_checker = 2
    is_prime = True

    while prime_checker <= sqrt(num):
        if num % prime_checker == 0:
            is_prime = False
            break
        prime_checker += 1

    if is_prime:
        prime_digits += [num]

# checking if number digits are in the list of the prime digits
has_prime = False
for digit in digits:
    if digit in prime_digits:
        print(digit, end=" ")
        has_prime = True

if has_prime:
    print("digits are primes in " + n)
else:
    print(n + " has no prime digits")