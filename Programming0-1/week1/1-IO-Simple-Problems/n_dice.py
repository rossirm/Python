__author__ = 'Боян'
from random import randint

dice_sides = input("How many sides the die will have ?")
dice_sides = int(dice_sides)

print("You rolled " + str(randint(1, dice_sides)))