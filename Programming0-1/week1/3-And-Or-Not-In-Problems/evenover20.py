__author__ = 'Боян'

n = input("Enter a number")
number = int(n)

is_even = number % 2 == 0
is_greater = number > 20

if is_even and is_greater:
    print("Yes it is!")
else:
    print("No it isn't")