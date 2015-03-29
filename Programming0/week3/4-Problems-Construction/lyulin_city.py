__author__ = 'Боян'


def blocks_seen(heights):
    seen = 0
    highest = 0

    for block in heights:
        if block > highest:
            highest = block
            seen += 1
    return seen


print(blocks_seen([1, 5, 3, 2, 1, 8, 3, 4, 5]))