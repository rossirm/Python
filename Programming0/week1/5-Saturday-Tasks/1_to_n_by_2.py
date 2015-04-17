__author__ = 'Боян'

n = input("Enter a number")
number = int(n)

counter = 1
while counter <= number:
    if counter % 2 != 0:
        print(counter)
    counter += 1