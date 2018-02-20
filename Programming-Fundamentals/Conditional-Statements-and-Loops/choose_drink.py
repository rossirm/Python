profession = input()

drink = ''
if profession == 'Athlete':
    drink = 'Water'
elif profession == 'Businessman' or profession == 'Businesswoman':
    drink = 'Coffee'
elif profession == 'SoftUni Student':
    drink = 'Beer'
else:
    drink = 'Tea'

print(drink)
