__author__ = 'Боян'

a = input("Enter first digit")
b = input("Enter second digit")
c = input("Enter third digit")

is_single_char = len(a) == 1 and len(b) == 1 and len(c) == 1

if is_single_char:
    if a.isdigit() and b.isdigit() and c.isdigit():
        number = int(a + b + c)
        print(number)
else:
    print("Enter a single Digit [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
