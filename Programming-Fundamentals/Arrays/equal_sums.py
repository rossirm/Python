numbers = list(map(int, filter(None, input().split(' '))))

index = -1
for i in range(len(numbers)):
    left = sum(numbers[:i])
    right = sum(numbers[i + 1:])
    if left == right:
        index = i
print(index if index >= 0 else 'no')
