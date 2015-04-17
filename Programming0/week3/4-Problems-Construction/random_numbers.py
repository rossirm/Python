__author__ = 'Боян'
from random import randint


def generate_random_list(n, start, end):
    randoms = []
    for r in range(0, n):
        randoms += [randint(start, end)]

    return randoms


print(generate_random_list(5, 1, 3))