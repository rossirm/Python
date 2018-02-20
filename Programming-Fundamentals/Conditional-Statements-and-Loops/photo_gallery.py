from datetime import datetime

number = int(input())
day = int(input())
month = int(input())
year = int(input())
hours = int(input())
minutes = int(input())
size = int(input())
width = int(input())
height = int(input())

name = f'DSC_{number:04}.jpg'

date = datetime(year, month, day, hours, minutes).strftime('%d/%m/%Y %H:%M')

human_readable_size = ''
if size < 1000:
    human_readable_size = f'{size}B'
elif size < 1000000:
    human_readable_size = f'{(size/1000):g}KB'
else:
    human_readable_size = f'{(size/1000000):g}MB'

orientation = ''
if width > height:
    orientation = 'landscape'
elif width < height:
    orientation = 'portrait'
else:
    orientation = 'square'

info = f'Name: {name}\n' \
       f'Date Taken: {date}\n' \
       f'Size: {human_readable_size}\n' \
       f'Resolution: {width}x{height} ({orientation})'
print(info)
