import sys
import math

count = int(input())
maximal = -sys.maxsize
total = 0

for number in range(count):
    current = int(input())
    if current > maximal:
        maximal = current
    total += current
    
sum_of_others = math.fabs(total - maximal)
if sum_of_others == maximal:
    print('yes sum {}'.format(maximal))
elif sum_of_others != maximal:
    difference = math.fabs(sum_of_others - maximal)
    print('no diff {}'.format(difference))
