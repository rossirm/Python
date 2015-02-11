__author__ = 'Боян'

n = input("Enter a number")
num = int(n)
total = 0

while num > 0:
    total += num % 10
    num //= 10

print(total)