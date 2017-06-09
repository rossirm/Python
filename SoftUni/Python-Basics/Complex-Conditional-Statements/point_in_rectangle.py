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
