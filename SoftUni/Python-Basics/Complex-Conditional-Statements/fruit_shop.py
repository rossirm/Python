product = input().lower()
day = input().lower()
quantity = float(input())

order = 0
has_error = False
if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if product == 'banana':
        order = quantity * 2.5
    elif product == 'apple':
        order = quantity * 1.2
    elif product == 'orange':
        order = quantity * 0.85
    elif product == 'grapefruit':
        order = quantity * 1.45
    elif product == 'kiwi':
        order = quantity * 2.7
    elif product == 'pineapple':
        order = quantity * 5.5
    elif product == 'grapes':
        order = quantity * 3.85
    else:
        has_error = True
elif day == 'saturday' or day == 'sunday':
    if product == 'banana':
        order = quantity * 2.7
    elif product == 'apple':
        order = quantity * 1.25
    elif product == 'orange':
        order = quantity * 0.9
    elif product == 'grapefruit':
        order = quantity * 1.6
    elif product == 'kiwi':
        order = quantity * 3.0
    elif product == 'pineapple':
        order = quantity * 5.6
    elif product == 'grapes':
        order = quantity * 4.2
    else:
        has_error = True
else:
    has_error = True

if not has_error:
    print('{0:.2f}'.format(round(order, 2)))
else:
    print('Error')
