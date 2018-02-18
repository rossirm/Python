import sys

count = int(input())

maximal = -sys.maxsize
for number in range(count):
    current = int(input())
    if current > maximal:
        maximal = current

print(maximal)
