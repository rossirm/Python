numbers = list(map(float, filter(None, input().split(' '))))

i = 1
while i < len(numbers):
    if numbers[i - 1] == numbers[i]:
        numbers[i] = numbers[i] + numbers[i - 1]
        del numbers[i - 1]
        i = max(i - 1, 1)
    else:
        i += 1

print(' '.join([f'{str(number)}:g' for number in numbers]))
