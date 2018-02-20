month = input()
nights = int(input())

studio = 0.0
double = 0.0
master = 0.0

if month == 'May' or month == 'October':
    studio = 50.0
    double = 65.0
    master = 75.0
    if nights > 7:
        studio *= 0.95
elif month == 'June' or month == 'September':
    studio = 60.0
    double = 72.0
    master = 82.0
    if nights > 14:
        double *= 0.9
elif month == 'July' or month == 'August' or month == 'December':
    studio = 68.0
    double = 77.0
    master = 89.0
    if nights > 14:
        master *= 0.85

gets_free_night = nights > 7 and (month == 'September' or month == 'October')
result = f'Studio: {studio * (nights - 1):.2f} lv.\n' \
         f'Double: {double * nights:.2f} lv.\n' \
         f'Suite: {master * nights:.2f} lv.' \
    if gets_free_night \
    else f'Studio: {studio * nights:.2f} lv.\n' \
         f'Double: {double * nights:.2f} lv.\n' \
         f'Suite: {master * nights:.2f} lv.'
print(result)
