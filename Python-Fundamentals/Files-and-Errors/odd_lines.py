path = './Resources/01. Odd Lines/Input.txt'

with open(path, 'r') as f:
    odd_lines = [line for i, line in enumerate(f, start=0) if i % 2 == 1]

print(''.join(odd_lines))
