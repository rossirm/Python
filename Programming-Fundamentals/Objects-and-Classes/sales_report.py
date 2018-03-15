n = int(input())
report = {}
for s in range(n):
    town, product, quantity, price = input().split(' ')
    price, quantity = float(price), float(quantity)
    if town in report:
        report[town] += price * quantity
    else:
        report[town] = price * quantity

result = ''
for t in sorted(report):
    result += f'{t} -> {report[t]:.2f}\n'
print(result)
