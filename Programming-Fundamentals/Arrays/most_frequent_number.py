numbers = list(map(int, filter(None, input().split(' '))))

max_sequence = 0
max_number = numbers[0]

for i in range(len(numbers)):
    current_sequence = 0
    for n in range(i, len(numbers)):
        if numbers[i] == numbers[n]:
            current_sequence += 1

        if current_sequence > max_sequence:
            max_sequence = current_sequence
            max_number = numbers[i]

print(max_number)
