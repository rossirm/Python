from datetime import date

weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

day, month, year = input().split('-')
some_date = date(int(year), int(month), int(day))
print(weekdays[some_date.weekday()])
