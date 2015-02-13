__author__ = 'Боян'
from math import sqrt

n = input("Enter a number")
# getting the digits of the number
digits = []
for d in n:
    digits += d
# print (digits)
# getting all prime numbers lesser than 10
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
        prime_digits.append(num)
# print (prime_digits)
# checking whether the number's digits appear in the prime digits list
has_prime = False
for digit in digits:
    if int(digit) in prime_digits:
        print(digit, end=" ")
        has_prime = True
if has_prime:
    print("digits are primes in " + n)
else:
    print(n + " has no prime digits")