__author__ = 'Боян'


def max_score(beers, fries):
    score = 0
    brews = sorted(beers)
    potatoes = sorted(fries)

    for combo in range(0, len(beers)):
        score += brews[combo] * potatoes[combo]

    return score


print(max_score([10, 11], [1, 5]))  # == 65
print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))  # == 1442560