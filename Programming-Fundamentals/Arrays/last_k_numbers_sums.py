n = int(input())
k = int(input())

numbers = [1]
for i in range(1, n):
    start = max(0, i - k)
    end = i
    total = 0
    for n in range(start, end):
        total += numbers[n]

    numbers.append(total)

result = ' '.join([str(i) for i in numbers])
print(result)
