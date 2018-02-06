from math import sqrt


def get_distance(x_1, y_1, x_2, y_2):
    return sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

first = abs(get_distance(x1, y1, x2, y2))
second = abs(get_distance(x3, y3, x4, y4))
if first >= second:
    p1 = abs(get_distance(x1, y1, 0, 0))
    p2 = abs(get_distance(x2, y2, 0, 0))
    result = f'({x1:.15g}, {y1:.15g})({x2:.15g}, {y2:.15g})' if p1 <= p2 \
        else f'({x2:.15g}, {y2:.15g})({x1:.15g}, {y1:.15g})'
else:
    p3 = abs(get_distance(x3, y3, 0, 0))
    p4 = abs(get_distance(x4, y4, 0, 0))
    result = f'({x3:.15g}, {y3:.15g})({x4:.15g}, {y4:.15g})' if p3 <= p4 \
        else f'({x4:.15g}, {y4:.15g})({x3:.15g}, {y3:.15g})'
print(result)
