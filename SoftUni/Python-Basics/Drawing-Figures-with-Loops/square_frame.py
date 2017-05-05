count = int(input())

edge = '+ '
frame = '| '
new_line = '\n'
inner = ''
square = ''
for i in range(count - 2):
    inner += '- '
for s in range(count):
    if s == 0 or s == count - 1:
        square += edge + inner + edge + new_line
    else:
        square += frame + inner + frame + new_line

print(square)
