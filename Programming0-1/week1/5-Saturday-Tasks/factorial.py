__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

fact = 1
counter = 1

while counter <= num:
    fact *= counter
    counter += 1

print("{0} factorial is: {1}".format(num, fact))