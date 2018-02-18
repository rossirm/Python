count = int(input())

fill = '*'
wall = '|'
space = '-'
new_line = '\n'
roof_top = 2 if count % 2 == 0 else 1

house = ''
# Roof
for i in range(roof_top, count, 2):
    roof = roof_top
    house += space * ((count - i) // 2) + fill * i + space * ((count - i) // 2) + new_line
    roof += 2
# Middle
house += fill * count + new_line
# Bottom
for i in range(count // 2):
    house += wall + fill * (count - 2) + wall + new_line

print(house)
