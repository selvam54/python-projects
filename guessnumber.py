import random

print("********************************guess number game*********************************************")

#player choice
while True:
    playerchoice=input(("\n1\n2\n3\n4\n5 \nenter the any number "))

#computer choice
    list=[ "1","2","3","4","5"]
    computerchoice=random.choice(list)
    print("the computer choice is: ",computerchoice)


#comperission the two choices
    if playerchoice == computerchoice:
      print("you correctly guess the number")
      if playerchoice=="quit":
          break
    else:
      print("you are lose")

