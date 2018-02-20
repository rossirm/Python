name = input()
volume = int(input())
energy = int(input())
sugar = int(input())

label = f'{volume}ml {name}:\n{volume / 100 * energy:g}kcal, {volume / 100 * sugar:g}g sugars'
print(label)
