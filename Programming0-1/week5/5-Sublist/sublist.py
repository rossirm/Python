__author__ = 'Боян'


def sublist(list1, list2):
    is_sublist = False

    for i in range(0, len(list2)):
        if list2[i] == list1[0] and list2[i:i + len(list1)] == list1:
            is_sublist = True

    return is_sublist


print(sublist(["Python"], ["Python", "Django"]))
print(sublist(["Python", "Django"], ["Django", "Python"]))
print(sublist([1, 2], [1, 0, 1, 2, 2]))