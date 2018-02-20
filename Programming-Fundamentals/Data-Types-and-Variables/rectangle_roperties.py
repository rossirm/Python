from math import sqrt

width = float(input())
height = float(input())
perimeter = 2 * (width + height)
area = width * height
diagonal = sqrt(width ** 2 + height ** 2)

print(f'{perimeter:.15g}\n{area:.15g}\n{diagonal:.15g}')
