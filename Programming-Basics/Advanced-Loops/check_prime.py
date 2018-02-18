import math

number = int(input())
is_prime = True

if number < 2:
    is_prime = False
else:
    end = int(math.sqrt(number))
    for i in range(2, end + 1):
        if number % i == 0:
            is_prime = False
            break

print('Prime' if is_prime else 'Not Prime')
