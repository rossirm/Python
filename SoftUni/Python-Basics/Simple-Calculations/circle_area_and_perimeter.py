# Напишете програма, която чете от конзолата число r
# и пресмята и отпечатва лицето и периметъра на кръг / окръжност с радиус r.
import math

r = float(input())

area = math.pi * r * r
perimeter = 2 * math.pi * r

print('Area = {0}\nPerimeter = {1}'.format(area, perimeter))