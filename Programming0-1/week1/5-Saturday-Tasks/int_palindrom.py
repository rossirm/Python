__author__ = 'Боян'

n = input("Enter a number")
num = int(n)
result = 0

while num > 0:
    result = result * 10 + num % 10
    num //= 10

if int(n) == result:
    print("{0} is palindrome".format(result))
else:
    print("{0} is NOT palindrome".format(result))