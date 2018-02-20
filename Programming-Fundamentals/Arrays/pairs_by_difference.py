numbers = list(map(int, filter(None, input().split(' '))))
numbers.sort()
difference = int(input())

count = 0
for a in range(len(numbers)):
    for b in range(a + 1, len(numbers)):
        current_diff = abs(numbers[a] - numbers[b])
        if current_diff == difference:
            count += 1
        elif current_diff > difference:
            break
print(count)
