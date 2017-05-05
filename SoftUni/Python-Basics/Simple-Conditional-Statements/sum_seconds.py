first = int(input())
second = int(input())
third = int(input())

seconds_total = first + second + third
minutes = seconds_total / 60
seconds = seconds_total % 60

print('{0}:{1:02}'.format(int(minutes), seconds))
