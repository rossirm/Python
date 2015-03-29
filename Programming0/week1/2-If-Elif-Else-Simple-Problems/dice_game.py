__author__ = 'Боян'
from random import randint

dice_sides = input("How many sides the die will have ?")
dice_sides = int(dice_sides)

f_player = input("First player name")
s_player = input("Second player name")

f_roll = randint(1, dice_sides)
s_roll = randint(1, dice_sides)

print("{0} rolls {1}".format(f_player, f_roll))
print("{0} rolls {1}".format(s_player, s_roll))

if f_roll > s_roll:
    print("{0} wins !".format(f_player))
elif f_roll < s_roll:
    print("{0} wins !".format(s_player))
else:
    print("Draw game")