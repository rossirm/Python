def get_value(hand):
    ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits = {'S': 4, 'H': 3, 'D': 2, 'C': 1}

    value = 0
    for card in hand:
        rank = card[:-1]
        suit = card[-1:]
        value += ranks[rank] * suits[suit]
    return value


players = {}

line = input()
while line != 'JOKER':
    name, draw = line.split(': ')
    cards = list(set(draw.split(', ')))
    if name in players:
        players[name] += cards
    else:
        players[name] = cards

    line = input()

for p in players:
    print(f'{p}: {get_value(list(set(players[p])))}')
