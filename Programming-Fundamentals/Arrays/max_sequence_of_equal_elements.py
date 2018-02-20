numbers = list(map(int, filter(None, input().split(' '))))

max_sequence = 1
max_element = numbers[0]
current_sequence = 1
for i in range(1, len(numbers)):
    if numbers[i - 1] == numbers[i]:
        current_sequence += 1
    else:
        current_sequence = 1

    if current_sequence > max_sequence:
        max_sequence = current_sequence
        max_element = numbers[i]

print(f'{max_element} ' * max_sequence)
