__author__ = 'Боян'

n = input("Enter a number")
number = int(n)

if number == 0:
    print("{0} is zero".format(number))
elif number % 2 == 0:
    print("{0} is even".format(number))
elif number % 2 != 0:
    print("{0} is odd".format(number))