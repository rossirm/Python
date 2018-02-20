from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def build_point():
    coordinates = list(map(float, input().split(' ')))
    return Point(*coordinates)


def measure_distance(a, b):
    x = abs(a.x - b.x)
    y = abs(a.y - b.y)
    return sqrt(x ** 2 + y ** 2)


point_a = build_point()
point_b = build_point()
distance = measure_distance(point_a, point_b)
print(f'{distance:.3f}')
