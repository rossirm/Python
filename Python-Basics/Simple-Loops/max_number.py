# Напишете програма, която въвежда n цели числа (n > 0) и намира най-голямото измежду тях.
# Първо се въвежда броят числа n, а след това самите n числа, по едно на ред.
import sys

count = int(input())

maximal = -sys.maxsize
for number in range(count):
    current = int(input())
    if current > maximal:
        maximal = current

print(maximal)
