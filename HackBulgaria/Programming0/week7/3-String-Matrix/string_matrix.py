__author__ = 'Боян'


def join(delimiter, items):
    joined = ""
    for index in range(0, len(items)):
        if index == len(items) - 1:
            joined += str(items[index])
        else:
            joined += str(items[index]) + delimiter
    return joined


def string_matrix(matrix_width, strings):
    matrix = []
    for string in strings:
        if len(string) < matrix_width:
            matrix += [string + "X" * (matrix_width - len(string))]
        elif len(string) > matrix_width:
            matrix += [string[0:matrix_width]]
        else:
            matrix += [string]

    strings_matrix = ""
    for n in range(0, matrix_width):
        if matrix[n] == matrix[matrix_width - 1]:
            new_line = "| " + join(" | ", matrix[n]) + " |"
            strings_matrix += new_line
        else:
            new_line = "| " + join(" | ", matrix[n]) + " |\n"
            strings_matrix += new_line
    return strings_matrix


result = string_matrix(6, ["python", "gogo", "perl", "java", "haskell", "ruby0nRails"])
print(result)