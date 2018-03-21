base, decimal_number = list(map(int, input().split(' ')))

remainders = ''
while decimal_number > 0:
    remainders += str(decimal_number % base)
    decimal_number //= base

print(int(remainders[::-1]))
