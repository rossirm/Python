from datetime import date, timedelta

day, month, start_year = input().split('-')
start_date = date(int(start_year), int(month), int(day))

day, month, end_year = input().split('-')
end_year = int(end_year)
end_date = date(end_year, int(month), int(day))

holidays = [date(end_year, 1, 1), date(end_year, 3, 3), date(end_year, 5, 1), date(end_year, 5, 6),
            date(end_year, 5, 24), date(end_year, 9, 6), date(end_year, 9, 22), date(end_year, 11, 1),
            date(end_year, 12, 24), date(end_year, 12, 25), date(end_year, 12, 26)]

period = [start_date + timedelta(days=x) for x in range(0, (end_date - start_date).days + 1)]
print(sum(1 for day in period if day.weekday() < 5 and day not in holidays))
