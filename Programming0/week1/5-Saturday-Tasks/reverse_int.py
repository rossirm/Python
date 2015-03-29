__author__ = 'Боян'

n = input("Enter a number")
num = int(n)
result = 0

while num > 0:
    result = result * 10 + num % 10
    num //= 10

print("{0} <- reversed -> {1}".format(n, result))