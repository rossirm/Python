def raise_power(number, power):
    return number ** power


n = float(input())
p = float(input())
print(f'{raise_power(n, p):.14g}')
