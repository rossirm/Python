numbers = list(map(int, filter(None, input().split(' '))))

length = len(numbers)
while length > 1:
    condensed = []
    for i in range(length - 1):
        condensed.append(numbers[i] + numbers[i + 1])
    numbers = condensed
    length -= 1

print(numbers[0])
