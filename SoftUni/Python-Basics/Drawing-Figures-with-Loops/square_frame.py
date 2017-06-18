# Напишете програма, която въвежда цяло положително число n и чертае на конзолата квадратна рамка с размер n * n

count = int(input())

edge = '+ '
frame = '| '
new_line = '\n'

inner = ''
for i in range(count - 2):
    inner += '- '

square = ''
for s in range(count):
    if s == 0 or s == count - 1:
        square += edge + inner + edge + new_line
    else:
        square += frame + inner + frame + new_line

print(square)
