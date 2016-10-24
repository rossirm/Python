__author__ = 'Боян'


def count_zero_neighbours(numbers):
    index = 1
    count = 0

    while index < len(numbers):
        if numbers[index] + numbers[index - 1] == 0:
            count += 1
        index += 1

    return count


print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))