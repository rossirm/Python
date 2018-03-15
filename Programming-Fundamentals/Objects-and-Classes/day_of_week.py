from datetime import date
import calendar

day, month, year = input().split('-')
some_date = date(int(year), int(month), int(day))
print(calendar.day_name[some_date.weekday()])
