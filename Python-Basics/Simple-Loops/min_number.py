# Напишете програма, която въвежда n цели числа (n > 0) и намира най-малкото измежду тях.
# Първо се въвежда броят числа n, а след това самите n числа, по едно на ред.
import sys

count = int(input())

minimal = sys.maxsize
for number in range(count):
    current = int(input())
    if current < minimal:
        minimal = current

print(minimal)
