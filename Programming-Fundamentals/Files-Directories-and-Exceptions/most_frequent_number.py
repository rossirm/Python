def get_max_number(numbers):
    numbers = list(map(int, filter(None, numbers.split(' '))))

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

    return max_number


path = './Resources-Exercises/01. Most Frequent Number/'

with open(f'{path}input.txt', 'r') as f:
    lines = f.read().split('\n')

result = ''
for l in lines:
    result += f'{get_max_number(l)}\n'

with open(f'{path}output.txt', 'w') as output:
    output.write(result)
