product = input()
town = input()
quantity = float(input())

order = 0
if town == 'Sofia':
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

if town == 'Plovdiv':
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

if town == 'Varna':
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

print(round(order, 2))
