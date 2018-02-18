is_even = False
number = 1

while not is_even:
    try:
        number = int(input())
        is_even = number % 2 == 0
    except ValueError:
        print('Invalid number!')

print(number)
