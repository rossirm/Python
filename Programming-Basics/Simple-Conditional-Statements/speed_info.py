speed = float(input())

speed_info = ''
if speed <= 10:
    speed_info = 'slow'
elif 10.0 < speed <= 50:
    speed_info = 'average'
elif 50.0 < speed <= 150:
    speed_info = 'fast'
elif 150.0 < speed <= 1000:
    speed_info = 'ultra fast'
elif speed > 1000:
    speed_info = 'extremely fast'
else:
    speed_info = 'Near light speed, probably? ...'

print(speed_info)
