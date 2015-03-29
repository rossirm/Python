__author__ = 'Боян'

n = input("Enter a 3 digit number")

is_three_char = len(n) == 3

if is_three_char:
    if n[0].isdigit() and n[1].isdigit() and n[2].isdigit():
        a = int(n[0])
        b = int(n[1])
        c = int(n[2])

        first = max(a, b, c)
        last = min(a, b, c)

        middle = a
        if (first == a and last == b) or (first == b and last == a):
            middle = c
        elif (first == a and last == c) or (first == c and last == a):
            middle = b

        greatest = first * 100 + middle * 10 + last
        least = last * 100 + middle * 10 + first
        print("{0} {1}".format(greatest, least))
else:
    print("Enter a 3 Digit [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] number")
