import math

number = int(input())

for n in range(2, number + 1):
    is_prime = True
    end = int(math.sqrt(n)) + 1
    for i in range(2, end):
        if n % i == 0:
            is_prime = False
            break
    print(f'{n} -> {is_prime}')
