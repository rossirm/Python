import math

numbers = list(map(float, filter(None, input().split(' '))))

result = ''
for i in range(len(numbers)):
    if numbers[i] > 0:
        result += f'{numbers[i]:g} => {math.trunc((numbers[i] + 0.5)):g}\n'
    else:
        result += f'{numbers[i]:g} => {math.trunc((numbers[i] - 0.5)):g}\n'
print(result)
