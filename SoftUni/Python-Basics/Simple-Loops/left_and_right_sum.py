import math

count = int(input())

left_sum = 0
right_sum = 0
for l in range(count):
    left_sum += int(input())
for r in range(count):
    right_sum += int(input())

difference = math.fabs(left_sum - right_sum)
if difference == 0:
    print('yes sum {}'.format(right_sum))
else:
    print('no diff {}'.format(difference))
