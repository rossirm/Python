def check_sign(number):
    if number > 0:
        return f'The number {number} is positive.'
    elif number < 0:
        return f'The number {number} is negative.'
    else:
        return f'The number {number} is zero.'


n = int(input())
print(check_sign(n))
