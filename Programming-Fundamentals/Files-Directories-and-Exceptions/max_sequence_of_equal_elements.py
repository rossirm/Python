def get_max_equal(text):
    numbers = list(map(int, filter(None, text.split(' '))))

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

    return f'{max_element} ' * max_sequence


path = './Resources-Exercises/04. Max Sequence of Equal Elements/'

with open(f'{path}input.txt', 'r') as f:
    lines = f.read().split('\n')

result = ''
for l in lines:
    result += f'{get_max_equal(l)}\n'

with open(f'{path}output.txt', 'w') as output:
    output.write(result)
