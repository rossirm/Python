numbers = list(map(int, filter(None, input().split(' '))))

result = ''
if len(numbers) > 1:
    is_even = len(numbers) % 2 == 0
    middle = len(numbers) // 2
    result = f'{{{numbers[middle - 1]}}} {{{numbers[middle]}}}' if is_even \
        else f'{{{numbers[middle - 1]}}} {{{numbers[middle]}}} {{{numbers[middle + 1]}}}'
else:
    result = f'{{{numbers[0]}}}'

print(result)
