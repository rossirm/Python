import math

number = int(input())
# Setting 0 and 1 to False and 2 and above to True
sieve = [False, False] + [True] * (number - 1)

square = int(math.sqrt(number)) + 1
for i in range(2, square):
    if sieve[i]:
        p = 2
        while p * i <= number:
            sieve[p * i] = False
            p += 1

result = ''
for s in range(number + 1):
    if sieve[s]:
        result += f'{s} '
print(result)
