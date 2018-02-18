is_in_range = False

while not is_in_range:
    number = int(input('Еnter a number in the range [1...100]: '))
    is_in_range = 1 <= number <= 100
    if is_in_range:
        print(f'The number is: {number}')
        break
