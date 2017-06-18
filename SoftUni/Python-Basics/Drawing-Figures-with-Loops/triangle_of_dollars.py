# Да се напише програма, която въвежда число n и печата триъгълник от долари

count = int(input())

dollar = '$'
space = ' '
new_line = '\n'

triangle = ''
for i in range(1, count + 1):
    triangle += '{0}{1}'.format(i * (dollar + space), new_line)

print(triangle)
