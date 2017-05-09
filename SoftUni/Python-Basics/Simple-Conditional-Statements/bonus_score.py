# Дадено е цяло число – брой точки. Върху него се начисляват бонус точки по правилата, описани по-долу.
# Да се напише програма, която пресмята бонус точките за това число и общия брой точки с бонусите.
# •	Ако числото е до 100 включително, бонус точките са 5.
# •	Ако числото е по-голямо от 100, бонус точките са 20% от числото.
# •	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
# •	Допълнителни бонус точки (начисляват се отделно от предходните):
# o	За четно число  + 1 т.
# o	За число, което завършва на 5  + 2 т.

score = int(input())

bonus = 0
# Set score in given ranges
if score > 1000:
    bonus = score * 0.1
elif score > 100:
    bonus = score * 0.2
elif score <= 100:
    bonus += 5
# additional scores
if score % 2 == 0:
    bonus += 1
if score % 10 == 5:
    bonus += 2

print('{0:g}\n{1:g}'.format(bonus, score + bonus))
