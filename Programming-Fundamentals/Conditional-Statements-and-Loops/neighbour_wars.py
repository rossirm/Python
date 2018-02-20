pesho_damage = int(input())
pesho_health = 100

gosho_damage = int(input())
gosho_healt = 100
turn = 1
have_tko = gosho_healt <= 0 or pesho_health <= 0
commentary = ''
while pesho_health > 0 and gosho_healt > 0:
    if turn % 2 == 0:
        pesho_health -= gosho_damage
        if pesho_health > 0:
            commentary += f'Gosho used Thunderous fist and reduced Pesho to {pesho_health} health.\n'
        else:
            commentary += f'Gosho won in {turn}th round.'
            break
    else:
        gosho_healt -= pesho_damage
        if gosho_healt > 0:
            commentary += f'Pesho used Roundhouse kick and reduced Gosho to {gosho_healt} health.\n'
        else:
            commentary += f'Pesho won in {turn}th round.'
            break
    if turn % 3 == 0:
        gosho_healt += 10
        pesho_health += 10
    turn += 1

print(commentary)
