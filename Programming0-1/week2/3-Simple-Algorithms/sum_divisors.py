__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

divisors = 0

counter = 1
while counter < num:
    if num % counter == 0:
        divisors += counter
    counter += 1

print("The sum of the divisors of {0} is : {1}".format(num, divisors))