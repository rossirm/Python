ingredients = filter(None, input().split(' '))
length = int(input())

useful = [i for i in ingredients if len(i) == length]
count = min(10, len(useful))

recipe = ''
for i in range(count):
    recipe += f'Adding {useful[i]}.\n'

used = ', '.join(useful[:count])
recipe += f'Made pizza with total of {count} ingredients.\n' \
          f'The ingredients are: {used}.'
print(recipe)
