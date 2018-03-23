path = './Resources/02. Line Numbers/'

with open(f'{path}Input.txt', 'r') as f:
    lines = f.read().split('\n')
    lines_numbered = '\n'.join([f'{i + 1}. {l}' for i, l in enumerate(lines) if l])

open(f'{path}Output.txt', 'w').write(lines_numbered)
