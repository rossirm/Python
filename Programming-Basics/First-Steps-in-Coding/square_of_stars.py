square_side = int(input())

star = '*'
space = ' '
empty_space = (square_side - 2) * space

square = ''
for row in range(1, square_side + 1):
    # check whether is first or last row
    if row == 1 or row == square_side:
        square += f'{star * square_side}\n'
    else:
        square += f'{star}{empty_space}{star}\n'

print(square)
