health = int(input())
virus = input()
virus_list = []
current_hp = health
result = ''
while virus != 'end':
    virus_str = int(sum([ord(c) for c in virus]) / 3)
    if virus in virus_list:
        virus_seconds = int(virus_str * len(virus) / 3)
    else:
        virus_seconds = virus_str * len(virus)
    result += f'Virus {virus}: {virus_str} => {virus_seconds} seconds\n'

    current_hp -= virus_seconds
    if current_hp > 0:
        virus_time = f'{virus_seconds // 60}m {virus_seconds % 60}s'
        result += f'{virus} defeated in {virus_time}.\n' \
                  f'Remaining health: {current_hp}\n'

        regeneration = int(0.2 * current_hp)
        current_hp = current_hp + regeneration if current_hp + regeneration <= health else health
        virus_list.append(virus)
        virus = input()
    else:
        result += f'Immune System Defeated.'
        break

if current_hp > 0:
    result += f'Final Health: {current_hp}'
print(result)
