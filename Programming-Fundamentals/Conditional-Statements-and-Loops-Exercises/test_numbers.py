first = int(input())
second = int(input())
boundary = int(input())

combinations = 0
total = 0
for a in range(first, 0, -1):
    if total >= boundary:
        break
    for b in range(1, second + 1):
        combinations += 1
        total += a * b * 3
        if total >= boundary:
            break

result = f'{combinations} combinations\nSum: {total}'
if total >= boundary:
    result += f' >= {boundary}'
print(result)
