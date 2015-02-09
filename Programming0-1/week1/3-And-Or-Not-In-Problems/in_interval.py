__author__ = 'Боян'

a = input("Lower bound of the interval")
a = int(a)
b = input("Upper bound of the interval")
b = int(b)
x = input("Enter a number to be checked")
x = int(x)

if a <= x <= b:
    if x == a:
        print("The number is equal to the lower bound of the interval")
    elif x == b:
        print("The number is equal to the upper bound of the interval")
    else:
        print("The number is in the interval")
else:
    if x < a:
        print("The number is outside the interval, x < a")
    elif x > b:
        print("The number is outside the interval, x > b")