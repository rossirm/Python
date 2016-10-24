__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

divisors = []

counter = 1
while counter < num:
    if num % counter == 0:
        divisors += [counter]
    counter += 1

print("The divisors of {0} are :".format(num))
for divisor in divisors:
    print(divisor)