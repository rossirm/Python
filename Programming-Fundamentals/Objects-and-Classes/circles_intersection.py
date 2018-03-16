from math import sqrt


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    @staticmethod
    def build_circle():
        x, y, r = list(map(float, input().split(' ')))
        return Circle(x, y, r)

    def do_intersect(self, other_circle):
        center_distance = sqrt(abs(self.x - other_circle.x) ** 2 + abs(self.x - other_circle.y) ** 2)
        return center_distance <= self.r + other_circle.r


first = Circle.build_circle()
second = Circle.build_circle()
print('Yes' if first.do_intersect(second) else 'No')
