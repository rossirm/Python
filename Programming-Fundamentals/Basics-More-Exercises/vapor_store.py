games = {'OutFall 4': 39.99,
         'CS: OG': 15.99,
         'Zplinter Zell': 19.99,
         'Honored 2': 59.99,
         'RoverWatch': 29.99,
         'RoverWatch Origins Edition': 39.99}
balance = float(input())
game = input()

spent = 0
message = ''
while game != 'Game Time':
    if game in games:
        price = games[game]
        if price > balance - spent:
            message += 'Too Expensive\n'
        else:
            message += f'Bought {game}\n'
            spent += price
    else:
        message += 'Not Found\n'

    if balance == spent:
        message += 'Out of money!'
        break
    game = input()

if balance > spent:
    message += f'Total spent: ${spent:.2f}. Remaining: ${(balance - spent):.2f}'

print(message)
