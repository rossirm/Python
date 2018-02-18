count = int(input())

space = ' '
side = '* '
new_line = '\n'

rhombus = ''
# Upper Part
for row in range(1, count):
    fill = space * (count - row)
    inner = side * row
    rhombus += fill + inner + fill + new_line
# Lower Part
for row in range(count, 0, -1):
    fill = space * (count - row)
    inner = side * row
    rhombus += fill + inner + fill + new_line

print(rhombus)
