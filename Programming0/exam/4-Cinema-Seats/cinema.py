__author__ = 'Боян'


def row_to_fill(seats):
    most_unoccupied = -1
    row_most = -1
    for row in range(0, len(seats)):
        current_row_seats = 0
        for seat in seats[row]:
            current_row_seats += seat

        if current_row_seats > most_unoccupied and current_row_seats != len(seats[row]):
            most_unoccupied = current_row_seats
            row_most = row
    return row_most


def have_empty_seats(rows):
    have_seats = False
    for row in rows:
        for seat in row:
            if seat == 0:
                return True
    return have_seats


def order_of_seats(cinema):
    order = []
    while have_empty_seats(cinema):
        next_row = row_to_fill(cinema)
        for seat in range(len(cinema[next_row])):
            if cinema[next_row][seat] == 0:
                cinema[next_row][seat] = 1
                order += [(next_row + 1, seat + 1)]

    return order


print(order_of_seats([[1, 1, 1, 0],
                      [1, 0, 1, 0],
                      [0, 0, 0, 0],
                      ]))
# [(1, 4), (2, 2), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4)]
print(order_of_seats([[1, 1, 1],
                      [1, 0, 0],
                      [1, 0, 0],
                      [1, 1, 0]]))
# [(4, 3), (2, 2), (2, 3), (3, 2), (3, 3)]
print(order_of_seats([[0, 0],
                      [0, 0],
                      [0, 0]]))
# [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]