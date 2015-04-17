__author__ = 'Боян'
from math import sqrt


def is_triangle(a, b, c):
    forms_triangle = a + b > c and a + c > b and c + b > a
    return forms_triangle


def area(a, b, c):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def is_pythagorean(a, b, c):
    pythagorean = a ** 2 + b ** 2 == c ** 2
    return pythagorean


def max_area(triangles):
    max_s = 0
    max_triangle = []
    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]
        s = area(a, b, c)

        if s >= max_s:
            max_s = s
            max_triangle = triangle
    return max_triangle, max_s


print(max_area([[3, 4, 5], [7, 8, 9]]))