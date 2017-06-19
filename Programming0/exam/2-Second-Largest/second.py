__author__ = 'Боян'


def second_largest(numbers):
    nums = sorted(numbers, reverse=True)
    has_second = False

    if len(nums) == 0:
        return has_second

    largest = nums[0]
    for n in nums:
        if largest > n:
            return n

    if not has_second:
        return has_second


print(second_largest([]))
# False
print(second_largest([2, 1]))
# 1
print(second_largest([5, 5]))
# False
print(second_largest([100, 100, 90]))
# 90
