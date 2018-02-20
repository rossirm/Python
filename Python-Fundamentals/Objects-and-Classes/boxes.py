from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def measure_distance(self, other_point):
        x = abs(self.x - other_point.x)
        y = abs(self.y - other_point.y)
        return sqrt(x ** 2 + y ** 2)


class Box:
    def __init__(self, box_points):
        self.upper_left = box_points[0]
        self.upper_right = box_points[1]
        self.bottom_left = box_points[2]
        self.bottom_right = box_points[3]
        self.width = Point.measure_distance(self.upper_left, self.upper_right)
        self.height = Point.measure_distance(self.upper_left, self.bottom_left)
        self.area = self.width * self.height
        self.perimeter = (self.width + self.height) * 2
        self.info = f'Box: {int(self.width)}, {int(self.height)}\n' \
                    f'Perimeter: {int(self.perimeter)}\nArea: {int(self.area)}'

    def get_info(self):
        return self.info


boxes = []
line = input()
while line != 'end':
    coords = line.split(' | ')
    points = []
    for point in coords:
        x, y = list(map(int, point.split(':')))
        points.append(Point(x, y))
    boxes.append(Box(points))
    line = input()

for box in boxes:
    print(box.get_info())
