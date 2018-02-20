keyboard = {
    0: ' ', 2: 'abc', 3: 'def',
    4: 'ghi', 5: 'jkl', 6: 'mno',
    7: 'pqrs', 8: 'tuv', 9: 'wxyz'
}

characters = int(input())
message = ''
for i in range(characters):
    press = input()
    button = int(press[0])
    times = len(press) - 1
    character = keyboard[button][times]
    message += character
print(message)
