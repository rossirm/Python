count = int(input())

wall = '*'
space = '-'
new_line = '\n'

edge = 2 if count % 2 == 0 else 1
inner = edge
mid = (count - 1) // 2

diamond = ''
if count < 3:
    diamond += wall * edge
else:
    diamond += space * mid + wall * inner + space * mid + new_line
    for outer in range(mid - 1, -1, -1):
        diamond += space * outer + wall + space * inner + wall + space * outer + new_line
        inner += 2
    inner -= 4
    for outer in range(1, mid):
        diamond += space * outer + wall + space * inner + wall + space * outer + new_line
        inner -= 2
    diamond += space * mid + wall * edge + space * mid + new_line

print(diamond)
