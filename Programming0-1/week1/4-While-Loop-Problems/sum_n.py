__author__ = 'Боян'

n = input("Enter he N-th number")
n = int(n)

number = 1
summed = 0

while number <= n:
    summed += number
    number += 1

print("Sum = {}".format(summed))
