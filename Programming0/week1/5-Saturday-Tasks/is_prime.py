__author__ = 'Боян'
from math import sqrt

n = input("Enter a number")
num = int(n)

is_prime = True

if num == 1:
    is_prime = True

checker = 2
while checker < sqrt(num):
    if num % checker == 0:
        is_prime = False
        break
    checker += 1

if is_prime:
    print("{0} is prime".format(num))
else:
    print("{0} is not prime".format(num))