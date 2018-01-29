count = int(input())
calories = 0

for i in range(count):
    ingredient = input().lower()
    if ingredient == 'cheese':
        calories += 500
    elif ingredient == 'tomato sauce':
        calories += 150
    elif ingredient == 'salami':
        calories += 600
    elif ingredient == 'pepper':
        calories += 50

result = f'Total calories: {calories}'
print(result)
