__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

while num > 1:
    print(num % 10)
    num = int(num / 10)