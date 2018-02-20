ingredient = input()
recipe = []
while ingredient != 'Bake!':
    recipe.append(ingredient)
    ingredient = input()

cake = ''
for ingredient in recipe:
    cake += f'Adding ingredient {ingredient}.\n'
cake += f'Preparing cake with {len(recipe)} ingredients.'
print(cake)
