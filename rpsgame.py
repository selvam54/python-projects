import random


print("*****************************Wellcome To Rock Paper Sissor Game*****************************")

#********************PLAYER CHOICE********************
while 1>-1:
    playerchoice=input("enter the any rps \n ROCK\nPAPER\nSSISOR\nenter the rps:")
    #*********************COMPUTER CHOICE*******************
    list=["rock","paper","sissor"]
    computerchoice=random.randrange(len(list))
    print("computer choice is :",list[computerchoice])

#********************comperision the game*********************

    if playerchoice=="rock" and computerchoice=="sissor":
        print("you win")
    elif playerchoice=="paper" and computerchoice=="rock":
        print("you win the game")
    elif playerchoice=="sissor" and computerchoice=="paper":
        print("you win")
    else:
        print("computer win")