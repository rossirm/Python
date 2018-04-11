shells = {}

line = input()
while line != 'Aggregate':
    regions, size = line.split(' ')
    size = int(size)

    if regions not in shells:
        shells[regions] = []
    if size not in shells[regions]:
        shells[regions].append(size)

    line = input()

result = ''
for region in shells:
    sum_shells = sum(shells[region])
    shells_count = len(shells[region])
    giant_shell = sum_shells - sum_shells // shells_count
    sizes = ', '.join([str(number) for number in shells[region]])

    result += f'{region} -> {sizes} ({giant_shell})\n'

print(result)
