__author__ = 'Боян'
from math import sqrt


def fill_tetrahedron(edge):
    edge /= 10
    volume = sqrt(2) / 12 * edge ** 3
    return round(volume, 2)

print(fill_tetrahedron(100))