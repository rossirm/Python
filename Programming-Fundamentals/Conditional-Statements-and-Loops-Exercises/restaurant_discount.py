group = int(input())
package = input()

hall = ''
price = 0
discount = 0
if group <= 50:
    hall = 'Small Hall'
    price += 2500
elif 50 < group <= 100:
    hall = 'Terrace'
    price += 5000
elif 100 < group <= 120:
    hall = 'Great Hall'
    price += 7500

if package == 'Normal':
    price += 500
    discount = 0.95
elif package == 'Gold':
    price += 750
    discount = 0.9
elif package == 'Platinum':
    price += 1000
    discount = 0.85

total = (price * discount) / group
result = f'We can offer you the {hall}\nThe price per person is {total:.2f}$' if group <= 120 \
    else 'We do not have an appropriate hall.'
print(result)
