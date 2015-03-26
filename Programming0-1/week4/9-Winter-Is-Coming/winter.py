__author__ = 'Боян'


def winter_is_coming(seasons):
    last_winter = 0

    for season in seasons:
        if season == "winter":
            last_winter = 0
        else:
            last_winter += 1

    return last_winter >= 5


print(winter_is_coming(["spring", "winter", "winter", "spring", "winter", "winter", "winter"]))