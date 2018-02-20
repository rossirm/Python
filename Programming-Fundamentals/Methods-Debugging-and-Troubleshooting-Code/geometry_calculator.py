from math import pi


def get_triangle_area():
    side = float(input())
    height = float(input())
    return side * height / 2


def get_square_area():
    side = float(input())
    return side ** 2


def get_rectangle_area():
    width = float(input())
    height = float(input())
    return width * height


def get_circle_area():
    radius = float(input())
    return pi * radius ** 2


figure = input()
result = ''
if figure == 'triangle':
    result = f'{get_triangle_area():.2f}'
elif figure == 'square':
    result = f'{get_square_area():.2f}'
elif figure == 'rectangle':
    result = f'{get_rectangle_area():.2f}'
elif figure == 'circle':
    result = f'{get_circle_area():.2f}'
print(result)
