# Напишете конзолна програма, която чете име на град (стринг)
# и обем на продажби (десетично число)
# и изчислява и извежда размера на търговската комисионна

town = input().lower()
sales = float(input())

commission = 0
has_error = False

if town == 'sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 <= sales <= 1000:
        commission = 0.07
    elif 1000 <= sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12
    else:
        has_error = True
elif town == 'varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 <= sales <= 1000:
        commission = 0.075
    elif 1000 <= sales <= 10000:
        commission = 0.1
    elif sales > 10000:
        commission = 0.13
    else:
        has_error = True
elif town == 'plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 <= sales <= 1000:
        commission = 0.08
    elif 1000 <= sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145
    else:
        has_error = True
else:
    has_error = True

if not has_error:
    print('{0:.2f}'.format(round(commission * sales, 2)))
else:
    print('error')
