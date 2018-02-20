profession = input()
quantity = int(input())

price = 0
if profession == 'Athlete':
    price = 0.7 * quantity
elif profession == 'Businessman' or profession == 'Businesswoman':
    price = 1 * quantity
elif profession == 'SoftUni Student':
    price = 1.7 * quantity
else:
    price = 1.2 * quantity

result = f'The {profession} has to pay {price:.2f}.'
print(result)
