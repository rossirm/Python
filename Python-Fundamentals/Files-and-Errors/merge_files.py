path = './Resources/03. Merge Files/'

with open(f'{path}FileOne.txt', 'r') as one, \
        open(f'{path}FileTwo.txt', 'r') as two, \
        open(f'{path}Output.txt', 'w') as out:
    file_one_lines = one.read().split('\n')
    file_two_lines = two.read().split('\n')

    result = '\n'.join(list(sorted(file_one_lines + file_two_lines)))

    out.write(result)
