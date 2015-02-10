__author__ = 'Боян'

number = input("Enter a number")
number = int(number)

counter = 1
while counter <= number:
    if counter % 2 != 0:
        print(counter)
    counter += 1