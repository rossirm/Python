import sys

count = int(input())

minimal = sys.maxsize
for number in range(count):
    current = int(input())
    if current < minimal:
        minimal = current

print(minimal)
