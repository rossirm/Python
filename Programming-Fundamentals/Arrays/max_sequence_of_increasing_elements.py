numbers = list(map(int, filter(None, input().split(' '))))

max_sequence = 1
max_index = 0
current_sequence = 1
for i in range(1, len(numbers)):
    if numbers[i - 1] < numbers[i]:
        current_sequence += 1
    else:
        current_sequence = 1

    if current_sequence > max_sequence:
        max_sequence = current_sequence
        max_index = i

result = numbers[(max_index - max_sequence + 1):(max_index + 1)]
print(' '.join([str(i) for i in result]))
