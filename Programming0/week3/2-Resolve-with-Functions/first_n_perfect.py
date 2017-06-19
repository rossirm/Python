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


def sum_divisors(divs):
    return sum_ints(divisors(divs))


def is_perfect(number):
    perfect = False
    if sum_divisors(number) == number:
        perfect = True
    return perfect


def first_n_perfects(nth):
    perfect = []

    perfect_counter = 0
    current_num = 1

    while perfect_counter < nth:
        current = is_perfect(current_num)
        if current:
            perfect += [current_num]
            perfect_counter += 1
        current_num += 1

    return perfect


n = input("Enter a number")
print(first_n_perfects(int(n)))