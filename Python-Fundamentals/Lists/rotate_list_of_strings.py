strings = input().split(' ')
rotated = strings

last = rotated.pop()
rotated.insert(0, last)

print(' '.join(rotated))
