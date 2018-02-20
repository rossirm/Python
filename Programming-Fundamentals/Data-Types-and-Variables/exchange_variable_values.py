first = int(input())
second = int(input())
print(f'Before:\na = {first}\nb = {second}')

first = first + second
second = first - second
first = first - second
print(f'After:\na = {first}\nb = {second}')
