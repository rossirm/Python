__author__ = 'Боян'

n = input("Enter a number")
num = int(n)

divisors_sum = 0
is_perfect = False

counter = 1
while counter < num:
    if num % counter == 0:
        divisors_sum += counter
    counter += 1

is_perfect = num == divisors_sum

if is_perfect:
    print("{0} is perfect\nSum of the divisors : {1}".format(num, divisors_sum))
else:
    print("{0} is NOT perfect\nSum of the divisors : {1}".format(num, divisors_sum))