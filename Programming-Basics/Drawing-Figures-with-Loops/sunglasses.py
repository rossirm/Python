count = int(input())

frame = '*'
lens = '/'
bridge = '|'
space = ' '
new_line = '\n'

glasses = ''
upper_lower = frame * (count * 2) + space * count + frame * (count * 2) + new_line
glasses += upper_lower
for i in range(count - 2):
    glass = frame + lens * (count * 2 - 2) + frame
    if i == (count - 3) // 2:
        glasses += glass + (bridge * count) + glass + new_line
    else:
        glasses += glass + (space * count) + glass + new_line
glasses += upper_lower

print(glasses)
