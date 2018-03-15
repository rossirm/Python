supermarket = {}
line = input()
while line != 'stocked':
    name, price, quantity = line.split(' ')
    price, quantity = float(price), int(quantity)
    if name not in supermarket:
        supermarket[name] = {'price': price, 'quantity': quantity}
    else:
        supermarket[name].update({'price': price})
        supermarket[name]['quantity']+=quantity
    line = input()
total = 0
result = ''
for product, stats in supermarket.items():
    result += f'{product}: ${stats["price"]:.2f} * {stats["quantity"]} = ${stats["price"] * stats["quantity"]:.2f}\n'
    total += stats["price"] * stats["quantity"]
result += f'{"-" * 30}\nGrand Total: ${total:.2f}'
print(result)
