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
