from math import sqrt


def get_face(x):
    return sqrt(x ** 2 * 2)


def get_space(x):
    return sqrt(x ** 2 * 3)


def get_volume(x):
    return x ** 3


def get_area(x):
    return x ** 2 * 6


side = float(input())
part = input()

result = ''
if part == 'face':
    result = f'{get_face(side):.2f}'
elif part == 'space':
    result = f'{get_space(side):.2f}'
elif part == 'volume':
    result = f'{get_volume(side):.2f}'
elif part == 'area':
    result = f'{get_area(side):.2f}'
print(result)
