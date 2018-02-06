from math import sqrt


def get_distance(x, y):
    return sqrt(x ** 2 + y ** 2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first = abs(get_distance(x1, y1))
second = abs(get_distance(x2, y2))
result = f'({x1:.15g}, {y1:.15g})' if first <= second else f'({x2:.15g}, {y2:.15g})'
print(result)
