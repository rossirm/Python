from math import sqrt


def check_prime(n):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        end = int(sqrt(n)) + 1
        for i in range(2, end):
            if n % i == 0:
                is_prime = False
                break
    return is_prime


first = int(input())
last = int(input())
primes = []
for p in range(first, last + 1):
    if check_prime(p):
        primes.append(p)

print(', '.join([str(x) for x in primes]))
