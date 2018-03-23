def count_symbols(text):
    count = {}
    for letter in text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    result = ''
    for key, value in sorted(count.items(), key=lambda x: x[1], reverse=True):
        result += f'{key} -> {value}\n'
    return result


path = './Resources-Exercises/03. Count of Symbols/'

with open(f'{path}input.txt', 'r') as f:
    line = f.readline()

with open(f'{path}output.txt', 'w') as output:
    output.write(count_symbols(line))
