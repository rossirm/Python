__author__ = 'Боян'
from math import sqrt


def tetrahedron_filled(tetrahedrons, water):
    counter = 0
    volume = 0
    for tetrahedron in tetrahedrons:
        current = 0
        tetrahedron /= 10
        current += sqrt(2) / 12 * tetrahedron ** 3
        if volume + current < water:
            volume += current
            counter += 1

    return counter


print(tetrahedron_filled([6, 100, 30], 10))