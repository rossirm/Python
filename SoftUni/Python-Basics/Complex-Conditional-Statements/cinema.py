projection = input().lower()
rows = int(input())
cols = int(input())

price = 0
if projection == 'premiere':
    price = 12
elif projection == 'normal':
    price = 7.5
elif projection == 'discount':
    price = 5

cost = round(price * rows * cols, 2)
print('{} leva', cost)
