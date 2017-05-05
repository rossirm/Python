score = int(input())

bonus = 0
# Set score in given ranges
if score > 1000:
    bonus = score * 0.1
elif score > 100:
    bonus = score * 0.2
elif score <= 100:
    bonus += 5

if score % 2 == 0:
    bonus += 1
if score % 10 == 5:
    bonus += 2

print ('{0:g}\n{1:g}'.format(bonus, score + bonus))
