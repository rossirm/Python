score = int(input())

bonus = 0
# set bonus according to score range
if score > 1000:
    bonus = score * 0.1
elif score > 100:
    bonus = score * 0.2
elif score <= 100:
    bonus += 5
# additional bonuses
if score % 2 == 0:
    bonus += 1
if score % 10 == 5:
    bonus += 2

print(f'{bonus:g}\n{(score + bonus):g}')
