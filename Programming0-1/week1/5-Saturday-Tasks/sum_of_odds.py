__author__ = 'Боян'

number = input("Enter a number")
number = int(number)

counter = 1
summed = 0
while counter <= number:
    if counter % 2 != 0:
        print(counter)
        summed += counter
    counter += 1

print(summed)