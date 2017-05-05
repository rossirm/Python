import time

hours = int(input())
minutes = int(input())

minutes += 15
hours += minutes / 60
hours %= 24
minutes %= 60

print('{0}:{1:02}'.format(int(hours), int(minutes)))
