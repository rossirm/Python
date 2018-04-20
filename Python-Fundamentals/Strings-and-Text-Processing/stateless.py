state = input()
fiction = input()

result = ''
while True:
    while fiction:
        state.strip()
        state = state.replace(fiction, '')
        if state:
            fiction = fiction[1:len(fiction) - 1]
        else:
            result += f'(void)\n'
            break
    result += f'{state}\n'

    state = input()
    if state != 'collapse':
        fiction = input()
    else:
        break

print(result)
