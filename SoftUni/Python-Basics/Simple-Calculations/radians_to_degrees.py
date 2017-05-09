# Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).
import math

radians = float(input())

degrees = radians * 180 / math.pi

print(round(degrees))
