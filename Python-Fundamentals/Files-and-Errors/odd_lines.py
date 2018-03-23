path = './Resources/01. Odd Lines/Input.txt'

f = open(path, 'r')
odd_lines = [line for i, line in enumerate(f, start=0) if i % 2 == 1]

print(''.join(odd_lines))
