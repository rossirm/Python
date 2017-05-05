import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = math.fabs(x1 - x2)
height = math.fabs(y1 - y2)
area = width * height
perimeter = (width + height) * 2

print ('{0}\n{1}'.format(area, perimeter))
