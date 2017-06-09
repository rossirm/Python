# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# •	Premiere – премиерна прожекция, на цена 12.00 лева.
# •	Normal – стандартна прожекция, на цена 7.50 лева.
# •	Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която въвежда тип прожекция (стринг),
# брой редове и брой колони в залата (цели числа)
# и изчислява общите приходи от билети при пълна зала

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