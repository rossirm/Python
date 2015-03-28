__author__ = 'Боян'


def str_reverse(string):
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += str(string[index])
        index -= 1
    return reversed_string


def trim_left(string):
    trimmed = ""
    for index in range(0, len(string)):
        if string[index] != " ":
            trimmed = string[index:len(string)]
            break
    return trimmed


def trim(string):
    trimmed_l = trim_left(string)
    trimmed_r = trim_left(str_reverse(trimmed_l))
    result = str_reverse(trimmed_r)
    return result


def inner_trim(string):
    outer_trimmed = trim(string)

    trimmed = outer_trimmed[0]
    for char in range(1, len(outer_trimmed)):
        if outer_trimmed[char] == " " and outer_trimmed[char - 1] == " ":
            continue
        else:
            trimmed += outer_trimmed[char]
    return trimmed


print(inner_trim("Python Django"))
print(inner_trim(" Python Django "))