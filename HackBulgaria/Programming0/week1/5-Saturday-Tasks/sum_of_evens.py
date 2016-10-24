__author__ = 'Боян'

n = input("Enter a number")
number = int(n)

counter = 1
total = 0

while counter <= number:
    if counter % 2 == 0:
        print(counter)
        total += counter
    counter += 1

print("The sum of all even numbers between 1 and {0} is: {1}".format(number, total))