square_side = int(input())

star = '*'
space = ' '
empty_space = (square_side - 2) * space

for number in range(square_side):
    if number == 0 or number == square_side - 1:
        print (star * square_side)
    else:
        print (star + empty_space + star)
