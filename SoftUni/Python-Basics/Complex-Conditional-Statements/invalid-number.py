# Дадено число е валидно, ако е в диапазона [100…200] или е 0.

number = int(input())

is_valid = (100 <= number <= 200) or number == 0
if not is_valid:
    print('invalid')
