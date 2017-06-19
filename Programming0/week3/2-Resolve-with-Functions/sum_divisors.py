__author__ = 'Боян'


def divisors(number):
    divs = []

    counter = 1
    while counter < number:
        if number % counter == 0:
            divs += [counter]
        counter += 1
    return divs


def sum_ints(numbers):
    summed = 0
    for num in numbers:
        summed += num
    return summed


n = input("Enter a number")
div_sum = sum_ints(divisors(int(n)))

print("The sum of the divisors of {0} is : {1}".format(n, div_sum))