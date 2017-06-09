# Да се напише конзолна програма, която въвежда възраст (десетично число) и пол (“m” или “f”) и отпечатва обръщение

age = float(input())
gender = input()

is_adult = age >= 16
title = ''
if gender == 'f':
    title = 'Ms.' if is_adult else 'Miss'
elif gender == 'm':
    title = 'Mr.' if is_adult else 'Master'

print(title)
