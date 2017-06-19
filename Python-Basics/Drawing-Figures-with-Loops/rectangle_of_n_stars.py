# Напишете програма, която въвежда цяло положително число n и печата на конзолата правоъгълник от n * n звездички

count = int(input())

star = '*'
new_line = '\n'

rectangle = ''
for i in range(count):
    rectangle += '{0}{1}'.format(count * star, new_line)

print(rectangle)
