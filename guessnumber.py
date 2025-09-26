import random

print("********************************guess number game*********************************************")
score=0
#player choice
while True:
    playerchoice=input(("\n1\n2\n3\n4\n5 \nenter the any number "))
    
    if playerchoice == "quit":
        break

#computer choice
    list=[ "1","2","3","4","5"]
    computerchoice=random.choice(list)
    print("the computer choice is: ",computerchoice)


#comperission the two choices
    if playerchoice == computerchoice:
      print("you correctly guess the number")
      score += 1
      
      if playerchoice=="quit":
          break
    else:
      print("you are lose")

    print("your score is : ",score)