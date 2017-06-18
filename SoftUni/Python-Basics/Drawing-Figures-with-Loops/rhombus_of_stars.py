# Напишете програма, която въвежда цяло положително число n и печата ромбче от звездички с размер n

count = int(input())

space = ' '
side = '*'
new_line = '\n'
rhombus = ''
# Upper Part
for row in range(1, count):
    fill = space * (count - row)
    inner = (space + side) * row
    rhombus += fill + inner + fill + new_line
# Lower Part
for row in range(count, 0, -1):
    fill = space * (count - row)
    inner = (space + side) * row
    rhombus += fill + inner + fill + new_line

print(rhombus)
