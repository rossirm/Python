BGN = 1
USD = 1.79549
EUR = 1.95583
GBP = 2.53405

amount = float(input())
input_currency = input()
output_currency = input()

money = amount
# Convert money in lev
if input_currency == 'BGN':
    money *= BGN
elif input_currency == 'USD':
    money *= USD
elif input_currency == 'EUR':
    money *= EUR
elif input_currency == 'GBP':
    money *= GBP

# Convert to wanted currency
if output_currency == 'BGN':
    money /= BGN
elif output_currency == 'USD':
    money /= USD
elif output_currency == 'EUR':
    money /= EUR
elif output_currency == 'GBP':
    money /= GBP

print(f'{money:.2f} {output_currency}')
