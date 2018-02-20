budget = float(input())
count = int(input())

cart = ''
spent = 0
for i in range(count):
    item = input()
    price = float(input())
    quantity = int(input())
    cart += f'Adding {quantity} {item}s to cart.\n' if quantity > 1 \
        else f'Adding {quantity} {item} to cart.\n'
    spent += price * quantity

cart += f'Subtotal: ${spent:.2f}\n'
cart += f'Money left: ${(budget - spent):.2f}' if budget - spent >= 0 \
    else f'Not enough. We need ${(abs(budget - spent)):.2f} more.'

print(cart)
