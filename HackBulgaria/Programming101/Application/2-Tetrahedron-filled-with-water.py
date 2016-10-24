__author__ = 'Боян'
from math import sqrt


def tetrahedron_filled(tetrahedrons, water):
    filled_count = 0
    volume = 0

    for tetrahedron in tetrahedrons:
        current = 0
        tetrahedron /= 10
        current += sqrt(2) / 12 * tetrahedron ** 3

        if volume + current < water:
            volume += current
            filled_count += 1

    return filled_count


print(tetrahedron_filled([6, 100, 30], 10))