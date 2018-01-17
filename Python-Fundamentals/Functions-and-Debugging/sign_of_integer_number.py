def check_sign(number):
    if number > 0:
        return f'The number {number} is positive.'
    elif number < 0:
        return f'The number {number} is negative.'
    else:
        return f'The number {number} is zero.'


print(check_sign(int(input())))
