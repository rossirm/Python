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


def is_perfect(number):
    perfect = False
    if sum_ints(divisors(number)) == number:
        perfect = True
    return perfect


n = input("Enter a number")
checked = is_perfect(int(n))

if checked:
    print("{0} is perfect Sum of the divisors is : {1}".format(int(n), sum_ints(divisors(int(n)))))
else:
    print("{0} is NOT perfect Sum of the divisors is : {1}".format(int(n), sum_ints(divisors(int(n)))))