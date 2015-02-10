__author__ = 'Боян'

n = input("Enter a number")
n = int(n)
summed = 0

while n > 1:
    summed += int(n % 10)
    n = int(n / 10)

print(summed)