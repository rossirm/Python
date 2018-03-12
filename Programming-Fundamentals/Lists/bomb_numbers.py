numbers = list(map(int, input().split(' ')))
length = len(numbers)
bomb, magnitude = list(map(int, input().split(' ')))
position = numbers.index(bomb) if bomb in numbers else -1

while position != -1:
    end = min(length - 1, position + magnitude)
    start = max(0, position - magnitude)

    numbers = numbers[:start] + numbers[end + 1:]
    position = numbers.index(bomb) if bomb in numbers else -1

print(sum(numbers))
