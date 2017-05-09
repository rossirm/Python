# Напишете програма за конвертиране на парична сума от една валута в друга.
# Трябва да се поддържат следните валути: BGN, USD, EUR, GBP.

BGN = 1
USD = 1.79549
EUR = 1.95583
GBP = 2.53405

value = float(input())
givenCurrency = input()
takenCurrency = input()

money = value
# Convert money in lev
if givenCurrency == 'BGN':
    money *= BGN
elif givenCurrency == 'USD':
    money *= USD
elif givenCurrency == 'EUR':
    money *= EUR
elif givenCurrency == 'GBP':
    money *= GBP

# Convert to wanted currency
if takenCurrency == 'BGN':
    money /= BGN
elif takenCurrency == 'USD':
    money /= USD
elif takenCurrency == 'EUR':
    money /= EUR
elif takenCurrency == 'GBP':
    money /= GBP

print('{0} {1}'.format(round(money, 2), takenCurrency))
