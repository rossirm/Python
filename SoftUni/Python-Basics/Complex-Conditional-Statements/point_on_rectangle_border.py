# Напишете програма, която проверява дали точка {x, y} се намира върху някоя от страните на
# правоъгълник {x1, y1} – {x2, y2}.
# Входните данни се четат от конзолата и се състоят от 6 реда:
# десетичните числа x1, y1, x2, y2, x и y (като се гарантира, че x1 < x2 и y1 < y2).

# Rectangle coordinates
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
# Point coordinates
x = float(input())
y = float(input())

is_lying_on_x = (x == x_1 or x == x_2) and (y_1 <= y <= y_2)
is_lying_on_y = (y == y_1 or y == y_2) and (x_1 <= x <= x_2)
is_on_border = is_lying_on_x or is_lying_on_y
result = ''
if is_on_border:
    result = 'Border'
else:
    result = 'Inside / Outside'

print(result)
