products = {}
result = ''

line = input()
while line != 'exam time':
    if line == 'shopping time':
        line = input()
        continue

    action, name, quantity = filter(None, line.split(' '))
    quantity = int(quantity)
    if action == 'stock':
        if name in products:
            products[name] += quantity
        else:
            products[name] = quantity
    elif action == 'buy':
        if name in products:
            if products[name] <= 0:
                result += f'{name} out of stock\n'
            else:
                products[name] -= quantity
        else:
            result += f'{name} doesn\'t exist\n'

    line = input()

for product, count in products.items():
    if count > 0:
        result += f'{product} -> {count}\n'

print(result)
