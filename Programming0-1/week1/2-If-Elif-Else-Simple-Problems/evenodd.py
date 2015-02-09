__author__ = 'Боян'

number = input("Enter a number")
number = int(number)

if number % 2 == 0:
    print("{0} is even".format(number))
else:
    print("{0} is odd".format(number))