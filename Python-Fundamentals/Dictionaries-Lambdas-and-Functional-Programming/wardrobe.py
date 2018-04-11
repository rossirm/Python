def fill_wardrobe(storage):
    count = int(input())
    for c in range(count):
        color, clothes = input().split(' -> ')
        if color not in storage:
            storage[color] = {}
        clothes = clothes.split(',')
        for clothing in clothes:
            if clothing in storage[color]:
                storage[color][clothing] += 1
            else:
                storage[color][clothing] = 1
    return storage


def search_wardrobe(storage, wear_color, wear_clothing):
    result = ''
    for color in storage:
        result += f'{color} clothes:\n'
        for clothing, count in storage[color].items():
            if color == wear_color and clothing == wear_clothing:
                result += f'* {clothing} - {count} (found!)\n'
            else:
                result += f'* {clothing} - {count}\n'
    print(result)


wardrobe = {}
fill_wardrobe(wardrobe)

colour, wear, *rest = input().split(' ', 2)
search_wardrobe(wardrobe, colour, wear)
