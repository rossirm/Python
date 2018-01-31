centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
milliseconds = seconds * 1000
microseconds = milliseconds * 1000
nanoseconds = microseconds * 1000

result = f'{centuries} centuries = {years} years = {days} days = {hours} ' \
         f'hours = {minutes} minutes = {seconds} seconds = {milliseconds} ' \
         f'milliseconds = {microseconds} microseconds = {nanoseconds} nanoseconds'
print(result)
