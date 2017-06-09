# Напишете програма, която чете от конзолата град (стринг),
# продукт (стринг)
# и количество (десетично число)
# и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

product = input().lower()
town = input().lower()
quantity = float(input())

order = 1
if town == 'sofia':
    if product == 'coffee':
        order = quantity * 0.5
    elif product == 'water':
        order = quantity * 0.8
    elif product == 'beer':
        order = quantity * 1.2
    elif product == 'sweets':
        order = quantity * 1.45
    elif product == 'peanuts':
        order = quantity * 1.6

elif town == 'plovdiv':
    if product == 'coffee':
        order = quantity * 0.4
    elif product == 'water':
        order = quantity * 0.7
    elif product == 'beer':
        order = quantity * 1.15
    elif product == 'sweets':
        order = quantity * 1.3
    elif product == 'peanuts':
        order = quantity * 1.5

elif town == 'varna':
    if product == 'coffee':
        order = quantity * 0.45
    elif product == 'water':
        order = quantity * 0.7
    elif product == 'beer':
        order = quantity * 1.1
    elif product == 'sweets':
        order = quantity * 1.35
    elif product == 'peanuts':
        order = quantity * 1.55

print('{0:.2f}'.format(round(order, 2)))
