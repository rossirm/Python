from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def build_point():
        x, y = list(map(float, input().split(' ')))
        return Point(x, y)

    @staticmethod
    def find_closest_points(points_list):
        distance = float('Infinity')
        points_count = len(points_list)
        closest_points = [points_list[0], points_list[1]]
        for a in range(points_count):
            for b in range(a + 1, points_count):
                current_distance = points_list[a].measure_distance(points_list[b])
                if current_distance < distance:
                    distance = current_distance
                    closest_points = [points_list[a], points_list[b]]
        return closest_points

    def measure_distance(self, other_point):
        return sqrt(abs(self.x - other_point.x) ** 2 + abs(self.y - other_point.y) ** 2)

    def print_coordinates(self):
        return f'({self.x:g}, {self.y:g})'


points = []
count = int(input())
for i in range(count):
    points.append(Point.build_point())

closest = Point.find_closest_points(points)
print(f'{closest[0].measure_distance(closest[1]):.3f}\n'
      f'{closest[0].print_coordinates()}\n'
      f'{closest[1].print_coordinates()}')
