__author__ = 'Боян'

n = input("Enter a number")
number = int(n)

counter = 1
total = 0

while counter <= number:
    if counter % 2 != 0:
        print(counter)
        total += counter
    counter += 1

print("The sum of all odd numbers between 1 and {} is: {}".format(number, total))