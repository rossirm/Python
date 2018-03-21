base, base_number = input().split(' ')
base = int(base)

decimal = 0
power = len(base_number) - 1
for digit in base_number:
    current_digit = int(digit)
    decimal += current_digit * base ** power
    power -= 1
print(decimal)
