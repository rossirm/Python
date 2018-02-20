operation = input()
result = 0
while operation != 'END':
    codes = operation.split(' ')
    if codes[0] == 'INC':
        result = int(codes[1]) + 1
    elif codes[0] == 'DEC':
        result = int(codes[1]) - 1
    elif codes[0] == 'ADD':
        result = int(codes[1]) + int(codes[2])
    elif codes[0] == 'MLA':
        result = int(codes[1]) * int(codes[2])
    operation = input()
print(result)
