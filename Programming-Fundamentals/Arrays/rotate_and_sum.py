numbers = list(map(int, filter(None, input().split(' '))))
rotations = int(input())

length = len(numbers)
totals = [0] * length
for r in range(1, rotations + 1):
    for i in range(length):
        position = (i + r) % length
        totals[position] += numbers[i]

result = ' '.join([str(i) for i in totals])
print(result)
