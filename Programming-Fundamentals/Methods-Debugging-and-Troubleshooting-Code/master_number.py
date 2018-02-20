def check_palindrome(x):
    num = str(x)
    end = len(num) - 1
    mid = end // 2 + 1
    is_palindrome = True
    for i in range(mid):
        if num[i] != num[end - i]:
            is_palindrome = False
            break
    return is_palindrome


def sum_digits(x):
    digits_sum = 0
    while x > 0:
        digits_sum += x % 10
        x //= 10
    return digits_sum % 7 == 0


def contains_even_digit(x):
    has_even = False
    while x > 0:
        if (x % 10) % 2 == 0:
            has_even = True
            break
        x //= 10
    return has_even


def check_master(x):
    return check_palindrome(x) and sum_digits(x) and contains_even_digit(x)


count = int(input()) + 1
result = ''
for n in range(1, count):
    if check_master(n):
        result += f'{n}\n'
print(result)
