__author__ = 'Боян'
from random import randint

dice_sides = input("How many sides the die will have ?")
dice_sides = int(dice_sides)

roll_1 = randint(1, dice_sides)
print("You rolled " + str(roll_1))
roll_2 = randint(1, dice_sides)
print("You rolled " + str(roll_2))
roll_3 = randint(1, dice_sides)
print("You rolled " + str(roll_3))

score = roll_1 + roll_2 + roll_3
print("Your score is " + str(score))