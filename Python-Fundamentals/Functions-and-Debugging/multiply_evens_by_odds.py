def evens_by_odds(number):
    number = normalize_input(number)
    return even_odd_product(number)


def normalize_input(number):
    return number[1:] if number[0] == '-' else number


def even_odd_product(number):
    evens = 0
    odds = 0
    for c in range(0, len(number)):
        current = int(number[c])
        if current % 2 == 0:
            evens += current
        elif current % 2 != 0:
            odds += current
    return evens * odds


i = input()
print(evens_by_odds(i))
