__author__ = 'Боян'


def magic_square(square):
    col_sum = 0
    row_sum = 0
    l_diagonal_sum = 0
    r_diagonal_sum = 0
    length = len(square[0])

    for pos in range(0, length):
        row_sum += square[0][pos]
        col_sum += square[pos][0]
        l_diagonal_sum += square[pos][pos]
        r_diagonal_sum += square[length-1 - pos][length-1 - pos]

    return row_sum == col_sum == l_diagonal_sum == r_diagonal_sum


square1 = [[23, 28, 21], [22, 24, 26], [27, 20, 25]]
square2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(magic_square(square1))
print(magic_square(square2))