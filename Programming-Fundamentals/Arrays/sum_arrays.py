first = list(map(int, filter(None, input().split(' '))))
second = list(map(int, filter(None, input().split(' '))))
length = max(len(first), len(second))

totals = []
for i in range(length):
    totals.append(first[i % len(first)] + second[i % len(second)])

result = ' '.join([str(i) for i in totals])
print(result)
