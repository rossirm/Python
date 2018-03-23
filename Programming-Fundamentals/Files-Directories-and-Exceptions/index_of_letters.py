def index_letter(word):
    a = 97

    result = ''
    for char in word:
        result += f'{char} -> {ord(char) - a}\n'
    return result


path = './Resources-Exercises/02. Index Of Letters/'

with open(f'{path}input.txt', 'r') as f:
    line = f.readline()

with open(f'{path}output.txt', 'w') as output:
    output.write(index_letter(line))
