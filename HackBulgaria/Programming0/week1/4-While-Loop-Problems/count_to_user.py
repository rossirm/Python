__author__ = 'Боян'

n = input("Enter he N-th number")
number = int(n)

print("Counting from 1 to {0}".format(number))
counter = 1
while counter <= number:
    print(counter)
    counter += 1

print("Counting from {0} to 1".format(number))
counter = number
while counter >= 1:
    print(counter)
    counter -= 1