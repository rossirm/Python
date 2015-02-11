__author__ = 'Боян'

n = input("Enter a number")
num = int(n)
mirror = 0

while num > 0:
    mirror = mirror * 10 + num % 10
    num //= 10

if int(n) == mirror:
    print("{0} is palindrome".format(mirror))
else:
    print("{0} is NOT palindrome".format(mirror))