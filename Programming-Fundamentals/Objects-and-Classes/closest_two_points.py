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


points = []
count = int(input())
for i in range(count):
    points.append(build_point())

distance = float('Infinity')
last_point = len(points)
closest_points = [0, 0]
for f in range(last_point):
    for s in range(f + 1, last_point):
        current_distance = measure_distance(points[f], points[s])
        if current_distance < distance:
            distance = current_distance
            closest_points = [f, s]

print(f'{distance:.3f}\n'
      f'({points[closest_points[0]].x:g}, {points[closest_points[0]].y:g})\n'
      f'({points[closest_points[1]].x:g}, {points[closest_points[1]].y:g})')
