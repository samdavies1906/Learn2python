# A rock paper scissors, lizard, spock game using dictionaries dictionaries

import os
import random

# Clear console each run
os.system('cls||clear')

# Dictionary of what moves beat what
winningMoves = {1 : [3,4],  #Rock crushes scissors and lizard
                2 : [1, 5], #Paper covers rock and disproves spock
                3 : [2, 4], #Scissors cuts paper and lizard
                4 : [5, 2], #Lizrad poisons spock and eats paper
                5 : [2, 5] } #Spock smashes scissors and vaporizes rock

# Move list
# Rock(1), Paper(2), Scissors(3), Lizard(4), Spock(5)
moveListNums = [1,2,3,4,5]
moveListNames = ["rock", "paper", "scissors", "lizard", "spock"]


while True:
    try:
        bestOf = int(input("Best of how many rounds?: "))
    except ValueError:
        print("Must enter a number")
        continue
    else:
        break

roundsToWin = (bestOf // 2) + 1
playerScore = 0
computerScore = 0

while playerScore < roundsToWin and computerScore < roundsToWin:
    # Player move

    while True:
        try:
            playerMove = int(input("pick Rock(1), Paper(2), Scissors(3), Lizard(4), Spock(5): "))
        except ValueError:
            print("Must enter a number")
            continue

        if not playerMove in moveListNums:
            print("Must enter a number 1-5")
        else:
            break

    # Computer move
    computerMove = random.choice(moveListNums)

    print(str(moveListNames[playerMove - 1]) + "   VS.   " + str(moveListNames[computerMove - 1]))

    if computerMove in winningMoves.get(playerMove):
        print("You Win!")
        playerScore += 1
    elif playerMove == computerMove:
        print("Its a draw")
    else:
        print("You lose")
        computerScore += 1

    print("You: " + str(playerScore) + "        Compuer: " + str(computerScore))

if playerScore == roundsToWin:
    print("You win!")
else:
    print("You Lost, Sadge :(")
