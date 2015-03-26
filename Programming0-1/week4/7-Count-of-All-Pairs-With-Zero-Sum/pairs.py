__author__ = 'Боян'


def count_zero_pairs(numbers):
    count = 0
    length = len(numbers)

    for x in range(0, length):
        for y in range(x, length):
            if numbers[x] + numbers[y] == 0:
                count += 1

    return count


print(count_zero_pairs([0, 2, -2, 5, 10]))