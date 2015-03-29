__author__ = 'Боян'


def head(items):
    return items[0]


def last(items):
    return items[len(items) - 1]


def tail(items):
    tails = []
    for index in range(1, len(items)):
        tails += [items[index]]
    return tails


def equal_lists(first, second):
    are_equal = True
    if len(first) == len(second):
        for index in range(len(first)):
            if first[index] != second[index]:
                are_equal = False
    else:
        are_equal = False
    return are_equal


def count_item(element, items):
    count = 0
    for member in items:
        if member == element:
            count += 1
    return count


def take(n, items):
    taken = []
    for index in range(0, min(len(items), n)):
        taken += [items[index]]
    return taken


def drop(n, items):
    dropped = []
    for index in range(n, len(items)):
        dropped += [items[index]]
    return dropped


def reverse(items):
    reversed_items = []
    index = len(items) - 1
    while index >= 0:
        reversed_items += [items[index]]
        index -= 1
    return reversed_items

# Tests

# # head
# print(head([1, 2, 3]))
# print(head(["Python"]))

# # last
# print(last([1, 2, 3]))
# print(last(["Python"]))

# # tail
# print(tail([1, 2, 3]))
# print(tail(["Python"]))

# # equal_lists
# print(equal_lists([1, 2], [1, 2]))
# print(equal_lists([1, 2], [2, 1]))
# print(equal_lists([], []))

# # count_item
# print(count_item(5, [1, 2, 3, 4, 5]))
# print(count_item("winter", ["winter", "winter"]))
# print(count_item(False, [True, True]))

# # take
# print(take(2, [1, 2, 3, 4, 5]))
# print(take(3, [3, 4, 5, 6, 7, 8]))
# print(take(10, [1]))

# # drop
# print(drop(1, [1, 2, 3]))
# print(drop(2, ["Python", "Ruby", "Django", "Rails"]))
# print(drop(10, [1]))

# reverse
print(reverse(["Speak", "in", "reverse", "you", "must!"]))
print(reverse([1, 2, 3]))
print(reverse([]))