__author__ = 'Боян'
from random import randint

dice_sides = input("How many sides the die will have ?")
dice_sides = int(dice_sides)

dice_roll = randint(1, dice_sides)

print("You rolled " + str(dice_roll))