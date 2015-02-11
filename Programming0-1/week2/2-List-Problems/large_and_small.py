__author__ = 'Боян'

n = input("Enter a number")
digits = []

counter = 0
while counter <= len(n) - 1:
    digits = digits + [n[counter]]
    counter += 1

digits.sort()

smallest = 0

counter = 0
while counter <= len(n) - 1:
    smallest *= 10
    smallest += int(digits[counter])
    counter += 1

biggest = 0

counter = len(n) - 1
while counter >= 0:
    biggest *= 10
    biggest += int(digits[counter])
    counter -= 1

print("Biggest  number from {0} is: {1}".format(n, biggest))
print("Smallest number from {0} is: {1}".format(n, smallest))