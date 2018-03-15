dragons = {}

count = int(input())
for d in range(count):
    d_type, name, damage, health, armor = input().split(' ')
    damage = 45 if damage == 'null' else int(damage)
    health = 250 if health == 'null' else int(health)
    armor = 10 if armor == 'null' else int(armor)

    if d_type not in dragons:
        dragons[d_type] = {name: {'damage': damage, 'health': health, 'armor': armor}}
    else:
        dragons[d_type].update({name: {'damage': damage, 'health': health, 'armor': armor}})

result = ''
for kind, entries in dragons.items():
    type_stats = {'count': 0, 'damage': 0, 'health': 0, 'armor': 0}
    type_info = ''

    for name, stats in sorted(entries.items()):
        type_info += f'-{name} -> damage: {stats["damage"]}, health: {stats["health"]}, armor: {stats["armor"]}\n'
        type_stats['damage'] += stats["damage"]
        type_stats['health'] += stats["health"]
        type_stats['armor'] += stats["armor"]
        type_stats['count'] += 1

    avg_dmg = type_stats['damage'] / type_stats['count']
    avg_hlt = type_stats['health'] / type_stats['count']
    avg_arm = type_stats['armor'] / type_stats['count']
    result += f'{kind}::({avg_dmg:.2f}/{avg_hlt:.2f}/{avg_arm:.2f})\n{type_info}'
print(result)