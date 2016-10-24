__author__ = 'Боян'


def forecast(days):
    weather = {
        "sunshine": 0,
        "rain": 0,
        "snow": 0,
    }

    for day in days:
        if day == "sunshine":
            weather["sunshine"] += 1
        elif day == "rain":
            weather["rain"] += 1
        elif day == "snow":
            weather["snow"] += 1

    most = 0
    for day in weather:
        if weather[day] > most:
            most = weather[day]

    # 3 are equal most
    if weather["sunshine"] == weather["rain"] == weather["snow"]:
        return days[len(days) - 1]
    # 2 are equal most
    elif weather["sunshine"] == weather["rain"] == most or weather["sunshine"] == weather["snow"] == most or weather["rain"] == weather["snow"] == most:
        for key in weather:
            if weather[key] != most:
                return key
                break
    # 1 is most
    else:
        for key in weather:
            if weather[key] == most:
                return key
                break


print(forecast(["snow", "snow", "rain", "sunshine"]))
print(forecast(["rain", "rain", "snow", "snow", "sunshine", "sunshine"]))
print(forecast(["rain", "rain", "sunshine", "sunshine"]))