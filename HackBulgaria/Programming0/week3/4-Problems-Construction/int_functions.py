__author__ = 'Боян'


def to_digits(n):
    digits = []
    for digit in str(n):
        digits += [int(digit)]

    return digits


def reverse_int(n):
    digits = to_digits(n)
    index = len(digits) - 1
    reverse = 0

    while index >= 0:
        reverse *= 10
        reverse += digits[index]
        index -= 1

    return reverse


def sum_digits(n):
    digits = to_digits(n)
    digit_sum = 0

    for digit in digits:
        digit_sum += digit

    return digit_sum


def product_digits(n):
    digits = to_digits(n)
    digit_product = 1

    for digit in digits:
        digit_product *= digit

    return digit_product


number = input("Enter a number")
num = int(number)

print("Reversed: {0}".format(reverse_int(num)))
print("Sum of digits: {0}".format(sum_digits(num)))
print("Product of digits {0}".format(product_digits(num)))