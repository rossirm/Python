# Да се напише програма, която въвежда размерите на геометрична фигура и пресмята лицето й.
# Фигурите са четири вида: квадрат (square), правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (square, rectangle, circle или triangle).
# Ако фигурата е квадрат, на следващия ред се чете едно число – дължина на страната му.
# Ако фигурата е правоъгълник, на следващите два реда четат две числа – дължините на страните му.
# Ако фигурата е кръг, на следващия ред чете едно число – радиусът на кръга.
# Ако фигурата е триъгълник, на следващите два реда четат две числа –
# дължината на страната му и дължината на височината към нея.
# Резултатът да се закръгли до 3 цифри след десетичната точка.
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

print('{0:.3f}'.format(round(area, 3)))
