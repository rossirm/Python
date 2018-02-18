import math

figure = input()

area = 0
if figure == 'square':
    side = float(input())
    area = side * side
elif figure == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
elif figure == 'rectangle':
    width = float(input())
    height = float(input())
    area = width * height
elif figure == 'triangle':
    base_side = float(input())
    height = float(input())
    area = base_side * height / 2
else:
    print('No such figure!')

print(f'{area:.3f}')
