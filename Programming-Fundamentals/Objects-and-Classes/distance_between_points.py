from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def build_point():
        x, y = list(map(float, input().split(' ')))
        return Point(x, y)

    def measure_distance(self, other_point):
        return sqrt(abs(self.x - other_point.x) ** 2 + abs(self.y - other_point.y) ** 2)


first = Point.build_point()
second = Point.build_point()

print(f'{first.measure_distance(second):.3f}')
