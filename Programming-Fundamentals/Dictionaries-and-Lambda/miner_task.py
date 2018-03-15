mining = {}
resource = ''
quantity = 0
line_count = 0

line = input()
while line != 'stop':
    if line_count % 2 == 0:
        resource = line
    else:
        quantity = int(line)
        if resource in mining:
            mining[resource] += quantity
        else:
            mining[resource] = quantity

    line_count += 1
    line = input()

result = ''
for r, q in mining.items():
    result += f'{r} -> {q}\n'
print(result)
