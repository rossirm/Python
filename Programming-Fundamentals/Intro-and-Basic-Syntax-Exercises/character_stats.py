name = input()
current_health = int(input())
maximum_health = int(input())
current_energy = int(input())
maximum_energy = int(input())

current = '|'
missing = '.'
stats = f'Name: {name}\n' \
        f'Health: |{current*current_health}{missing*(maximum_health-current_health)}|' \
        f'\nEnergy: |{current*current_energy}{missing*(maximum_energy-current_energy)}|'
print(stats)
