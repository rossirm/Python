from datetime import date, timedelta

day, month, year = input().split('-')
start_date = date(int(year), int(month), int(day))

day, month, year = input().split('-')
end_date = date(int(year), int(month), int(day))

holidays = [date(int(year), 1, 1), date(int(year), 3, 3), date(int(year), 5, 1), date(int(year), 5, 6),
            date(int(year), 5, 24), date(int(year), 9, 6), date(int(year), 9, 22), date(int(year), 11, 1),
            date(int(year), 12, 24), date(int(year), 12, 25), date(int(year), 12, 26)]

period = [start_date + timedelta(days=x) for x in range(0, (end_date - start_date).days + 1)]
print(sum(1 for day in period if day.weekday() < 5 and day not in holidays))
