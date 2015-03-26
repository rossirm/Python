__author__ = 'Боян'


def travel_cost(travels):
    total = 0
    for travel in travels:
        if travel >= 23:
            travel = 23
        total += travel

    if total >= 50:
        total = 50

    return total


print(travel_cost([30, 28, 55]))