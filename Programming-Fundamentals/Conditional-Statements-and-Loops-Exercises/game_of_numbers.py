first = int(input())
second = int(input())
magic = int(input())

combinations = 0
has_magic = False
for a in range(first, second + 1):
    if has_magic:
        break
    for b in range(first, second + 1):
        combinations += 1
        if a + b == magic:
            has_magic = True
            break

result = f'Number found! {b} + {a-1} = {magic}' if \
    has_magic else f'{combinations} combinations - neither equals {magic}'
print(result)
