__author__ = 'Боян'


def fib_number(n):
    first = 1
    second = 1
    third = first + second

    fibonacci = []
    for fib in range(0, n):
        fibonacci += [first]
        first = second
        second = third
        third = first + second

    return fibonacci[n - 1]


print(fib_number(12))