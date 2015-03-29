__author__ = 'Боян'

n = input("Enter he N-th number")
number = int(n)

counter = 1
total = 0

while counter <= number:
    total += counter
    counter += 1

print("The sum of the numbers between 1 and {0} is: {1}".format(number, total))
