import random


print("*****************************Wellcome To Rock Paper Sissor Game*****************************")

#********************PLAYER CHOICE********************
while True:
   playerchoice=input("enter the any rps \n ROCK\nPAPER\nSCISSOR\nenter the rps:")
    #*********************COMPUTER CHOICE*******************
   list=["rock","paper","scissor"]
   computerchoice=random.choice(list)
   print("computer choice is",computerchoice)

#********************comperision the game*********************

   if playerchoice=="rock" and computerchoice=="scissor":
       print("you win")
   elif playerchoice=="paper" and computerchoice=="rock":
       print("you win the game")
   elif playerchoice=="scissor" and computerchoice=="paper":
       print("you win")
   elif playerchoice == computerchoice:
       print("It's a tie!")
   else:
       print("computer win")