path = './Resources/03. Merge Files/'

file_one_lines = open(f'{path}FileOne.txt', 'r').read().split('\n')
file_two_lines = open(f'{path}FileTwo.txt', 'r').read().split('\n')

result = '\n'.join(list(sorted(file_one_lines + file_two_lines)))
open(f'{path}Output.txt', 'w').write(result)
