products = {}
result = ''

line = input()
while line != 'exam time':
    if line == 'shopping time':
        line = input()
        continue

    action, name, quantity = filter(None, line.split(' '))
    if action == 'stock':
        if name in products:
            products[name] += int(quantity)
        else:
            products[name] = int(quantity)
    elif action == 'buy':
        if name in products:
            if products[name] <= 0:
                result += f'{name} out of stock\n'
            else:
                products[name] -= int(quantity)
        else:
            result += f'{name} doesn\'t exist\n'
    line = input()

for entry in products:
    if products[entry] > 0:
        result += f'{entry} -> {products[entry]}\n'
print(result)
