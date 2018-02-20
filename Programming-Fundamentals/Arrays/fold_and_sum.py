numbers = list(map(int, filter(None, input().split(' '))))

quarter = len(numbers) // 4
left = numbers[:quarter]
right = numbers[-quarter:]
folded = left[::-1] + right[::-1]
middle = numbers[quarter:(len(numbers) - quarter)]

for i in range(len(middle)):
    middle[i] += folded[i]
print(' '.join([str(i) for i in middle]))
