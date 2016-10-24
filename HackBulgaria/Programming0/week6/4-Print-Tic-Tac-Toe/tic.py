__author__ = 'Боян'


def join(delimiter, items):
    joined = ""
    for index in range(0, len(items)):
        if index == len(items) - 1:
            joined += str(items[index])
        else:
            joined += str(items[index]) + delimiter
    return joined


def board_to_string(board):
    board_string = ""
    for line in range(0, len(board)):
        if board[line] == board[len(board) - 1]:
            new_line = "| " + join(" | ", board[line]) + " |"
            board_string += new_line
        else:
            new_line = "| " + join(" | ", board[line]) + " |\n"
            board_string += new_line
    return board_string


print(13 * "=")
print(board_to_string([["X", "O", "#"], ["X", "X", "X"], ["#", "#", "#"]]))
print(13 * "=")