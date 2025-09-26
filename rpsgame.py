import random


print("*****************************Wellcome To Rock Paper Sissor Game*****************************")

#**********
#**********PLAYER CHOICE********************
choices=["rock","paper","scissor"]
player_score=0
computer_score=0
while True:
    
    playerchoice=input(f"\nROCK \u270A\nPAPER \u270B\nSCISSOR \u270C\nenter the rps : ").lower()
#quit section
    if playerchoice == "quit":
        break

   
    #*********************COMPUTER CHOICE*******************
    
    computerchoice=random.choice(choices)
    print("computer choice is : ",computerchoice)
    
#********************comperision the game*********************

    if playerchoice == computerchoice:
        print("tie the game")
    elif playerchoice not in choices:
        print("Invalid input! Please choose rock, paper, or scissor.")
        continue

    elif (playerchoice=="rock" and computerchoice=="scissor") or \
        (playerchoice=="paper" and computerchoice=="rock") or \
        (playerchoice=="scissor" and computerchoice=="paper"):
            
            print(f"you win ")
            player_score += 1
    else:
        print("computer win")
        computer_score += 1
    
    print("your score is : ",player_score,"\n computer score is : ",computer_score)   
       
