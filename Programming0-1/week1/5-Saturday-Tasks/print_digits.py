__author__ = 'Боян'

n = input("Enter a number")
n = int(n)

while n > 1:
    print(n % 10)
    n = int(n / 10)