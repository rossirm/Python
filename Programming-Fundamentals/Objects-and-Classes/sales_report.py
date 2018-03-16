class Sale:
    def __init__(self, town, product, quantity, price):
        self.town = town
        self.product = product
        self.quantity = quantity
        self.price = price

    @staticmethod
    def read_sale():
        town, product, quantity, price = input().split(' ')
        price, quantity = float(price), float(quantity)
        return Sale(town, product, quantity, price)


report = {}
n = int(input())
for s in range(n):
    some_sale = Sale.read_sale()
    if some_sale.town in report:
        report[some_sale.town] += some_sale.price * some_sale.quantity
    else:
        report[some_sale.town] = some_sale.price * some_sale.quantity

result = ''
for t in sorted(report):
    result += f'{t} -> {report[t]:.2f}\n'
print(result)
