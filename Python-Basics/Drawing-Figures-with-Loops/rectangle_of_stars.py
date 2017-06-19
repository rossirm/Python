# Напишете програма, която чертае на конзолата правоъгълник от 10 x 10 звездички

count = 10

star = '*'
new_line = '\n'

rectangle = ''
for i in range(count):
    rectangle += '{0}{1}'.format(count * star, new_line)

print(rectangle)
