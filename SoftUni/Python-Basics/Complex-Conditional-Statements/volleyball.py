year = input()
holidays = int(input())
home = int(input())

sofia_plays = (48 - home) * 3 / 4
holiday_plays = holidays * 2 / 3
plays = sofia_plays + home + holiday_plays
if year == 'leap':
    plays *= 1.15

print(int(plays))
