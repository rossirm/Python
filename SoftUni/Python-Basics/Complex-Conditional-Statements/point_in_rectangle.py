# Напишете програма, която проверява дали точка {x, y} се намира вътре в правоъгълник {x1, y1} – {x2, y2}.
# Входните данни се четат от конзолата и се състоят от 6 реда:
# десетичните числа x1, y1, x2, y2, x и y
# (като се гарантира, че x1 < x2 и y1 < y2).

# Rectangle coordinates
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
# Point coordinates
x = float(input())
y = float(input())

result = ''
if (x_1 <= x <= x_2) and (y_1 <= y <= y_2):
    result = 'Inside'
else:
    result = 'Outside'

print(result)
