hours = int(input())
minutes = int(input())

minutes += 15
hours += minutes / 60
hours %= 24
minutes %= 60

print(f'{int(hours)}:{int(minutes):02}')
