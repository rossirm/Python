__author__ = 'Боян'
from random import randint

maria_score = 1001
ivan_score = 1001
maria_wins = True
ivan_wins = True

while maria_wins or ivan_wins:
    counter = 1
    while counter <= 5:
        roll = randint(1, 6)

        if maria_score < 0:
            maria_score += roll
        elif maria_score - roll == 0:
            ivan_wins = False
            print("Maria Wins")
            break
        else:
            maria_score -= roll
        print("Maria" + str(maria_score))
        counter += 1

    counter = 1
    while counter <= 5:
        roll = randint(1, 6)

        if ivan_score < 0:
            ivan_score += roll
        elif ivan_score - roll == 0:
            maria_wins_wins = False
            print("Ivan Wins")
            break
        else:
            ivan_score -= roll
        print("Ivan Score" + str(ivan_score))
        counter += 1