__author__ = 'Боян'


def str_reverse(string):
    reversed_string = ""
    index = len(string) - 1
    while index >= 0:
        reversed_string += str(string[index])
        index -= 1
    return reversed_string


def join(delimiter, items):
    joined = ""
    for index in range(0, len(items)):
        if index == len(items) - 1:
            joined += str(items[index])
        else:
            joined += str(items[index]) + delimiter
    return joined


def startswith(search, string):
    length = len(search)
    is_starting = True
    for index in range(0, length):
        if string[index] != search[index]:
            is_starting = False
            break
    return is_starting


def endswith(search, string):
    is_ending = startswith(str_reverse(search), str_reverse(string))
    return is_ending


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


# Tests

# # str_reverse
# print(str_reverse("Python"))
# print(str_reverse("kapak"))
# print(str_reverse(""))

# # join
# print(join(" ", ["Radoslav", "Yordanov", "Georgiev"]))
# print(join("\n", ["line1", "line2"]))
# print(join("|", [1, 2, 3]))

# # startswith
# print(startswith("Py", "Python"))
# print(startswith("py", "Python"))
# print(startswith("baba", "asdbaba"))

# # endswith
# print(endswith(".py", "hello.py"))
# print(endswith("kapak", "babakapak"))
# print(endswith(" ", "Python "))
# print(endswith("py", "python"))

# trim
print(trim(" asda "))
print(trim(" spacious "))
print(trim("no here but yes at end "))
print(trim(" "))
print(trim("python"))