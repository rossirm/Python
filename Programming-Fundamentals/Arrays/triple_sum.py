numbers = list(map(int, filter(None, input().split(' '))))

is_found = False
for a in range(len(numbers)):
    for b in range(a + 1, len(numbers)):
        total = numbers[a] + numbers[b]
        if total in numbers:
            print(f'{numbers[a]} + {numbers[b]} == {total}')
            is_found = True

if not is_found:
    print('No')
