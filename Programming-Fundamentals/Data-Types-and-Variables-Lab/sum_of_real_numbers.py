from decimal import Decimal

count = int(input())

total = Decimal(0)
for i in range(count):
    total += Decimal(input())
print(total)
