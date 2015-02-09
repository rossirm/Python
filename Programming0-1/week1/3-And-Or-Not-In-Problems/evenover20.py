__author__ = 'Боян'

number = input("Enter a number")
number = int(number)

is_even = number % 2 == 0
is_greater = number > 20

if is_even and is_greater:
    print("Yes it is!")
else:
    print("No it isn't")