def get_digit_name(digit):
    digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
              5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    return digits[digit]


def get_last_digit(n):
    return n % 10


number = abs(int(input()))
english_name = get_digit_name(get_last_digit(number))
print(english_name)
