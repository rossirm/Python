day = input()
age = int(input())
price = 0
if day == 'Weekday':
    if 0 <= age <= 18:
        price = 12
    elif 18 < age <= 64:
        price = 18
    elif 64 < age <= 122:
        price = 12
elif day == 'Weekend':
    if 0 <= age <= 18:
        price = 15
    elif 18 < age <= 64:
        price = 20
    elif 64 < age <= 122:
        price = 15
elif day == 'Holiday':
    if 0 <= age <= 18:
        price = 5
    elif 18 < age <= 64:
        price = 12
    elif 64 < age <= 122:
        price = 10

result = f'{price}$' if price != 0 else 'Error!'
print(result)
