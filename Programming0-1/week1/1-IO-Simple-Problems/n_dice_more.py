__author__ = 'Боян'

from random import randint

dice_sides = input("How many sides the die will have ?")
dice_sides = int(dice_sides)
score = 0

for i in range(3):
    score += randint(1, dice_sides)

print(score)