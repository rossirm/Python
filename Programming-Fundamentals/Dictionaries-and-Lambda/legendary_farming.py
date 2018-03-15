farm = {'shards': 0, 'motes': 0, 'fragments': 0}
result = ''
has_legendary = False

line = input()
while True:
    grind = line.split(' ')
    for i in range(0, len(grind), 2):
        item = grind[i + 1].lower()
        quantity = int(grind[i])
        if item not in farm:
            farm[item] = quantity
        else:
            farm[item] += quantity

        if farm['shards'] >= 250:
            result += f'Shadowmourne obtained!\n'
            farm['shards'] -= 250
            has_legendary=True
            break
        elif farm['fragments'] >= 250:
            result += f'Valanyr obtained!\n'
            farm['fragments'] -= 250
            has_legendary = True
            break
        elif farm['motes'] >= 250:
            result += f'Dragonwrath obtained!\n'
            farm['motes'] -= 250
            has_legendary = True
            break
    if has_legendary:
        break
    line = input()

key = {i: q for i, q in farm.items() if i == 'shards' or i == 'fragments' or i == 'motes'}
junk = {i: q for i, q in farm.items() if i != 'shards' and i != 'fragments' and i != 'motes'}
key_sorted = sorted(key.items(), key=lambda x: (-x[1], x[0]))
junk_sorted = sorted(junk.items(), key=lambda x: x[0])
for i in key_sorted:
    result += f'{i[0]}: {i[1]}\n'
for j in junk_sorted:
    result += f'{j[0]}: {j[1]}\n'

print(result)
