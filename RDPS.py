import random
Player1_sum = 0
Player2_sum = 0
Dice11 = 0
Dice12 = 0
Dice21 = 0
Dice22 = 0
print("Player1 please roll your dice \n")
while True:

    while True:
        Dice11 = random.randint(0,6)
        Dice12 = random.randint(0,6)
        print("Dice 1 ={0} annd Dice 2 = {1}".format(Dice11,Dice12))
        if(Dice11==5) or (Dice12==5):
            print("Player 1: Your turn is over \n")
            print("Plater 2: It is now your turn  \n")
            break
        else:
            sum = Dice11 + Dice12
            Player1_sum += sum
            print("Player 1: Score {0}".format(Player1_sum))
            if(Player1_sum>=50):
                break

    if(Player1_sum>=50):
        break

    while True:
        Dice21 = random.randint(0,6)
        Dice22 = random.randint(0,6)
        print("Dice 1 = {0} and Dice 2 ={1}".format(Dice21,Dice22))
        if(Dice21==5) or (Dice22==5):
            print("Player 2: Your turn is over \n")
            print("Player 1: It is now your turn \n")
            break
        else:
            sum = Dice21 + Dice22
            Player2_sum += sum
            print("Player 2: Score {0}".format(Player2_sum))
            if (Player2_sum>=50):
                break

            if(Player1_sum>=50):
                break
        if(Player1_sum>=50):
            print()
            print("Winner is player 1")
            print("Player 1 final score: {0}".format(Player1_sum))
            print("Player 2 final score: {0}".format(Player2_sum))
        else:
            print()
            print("Winner is player 2")
            print("Player 1 final score: {0}".format(Player1_sum))
            print("Player 2 final score: {0}".format(Player2_sum))
            break            
