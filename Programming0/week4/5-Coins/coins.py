__author__ = 'Боян'


def calculate_coins(price):
    total = round(price * 100)
    coins = [100, 50, 20, 10, 5, 2, 1]

    paid = {}
    for coin in coins:
        coins_count = total // coin
        total -= coins_count * coin
        paid[coin] = coins_count

    return paid


print(calculate_coins(8.94))