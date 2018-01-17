def filled_square(size):
    return top_bottom(size) + middle_part(size) + top_bottom(size)


def top_bottom(size):
    return '-' * size * 2 + '\n'


def middle_part(size):
    middle = ''
    fill = '\/' * (size - 1)
    side = '-'
    row = f'{side}{fill}{side}\n'
    for r in range(2, size):
        middle += row
    return middle


print(filled_square(int(input())))
