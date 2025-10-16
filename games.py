from rpsgame import rpsplay
from guessnumber import gussnumberplay
from calculator import calculatorplay
from simplechatbot import simplechatbotplay

while True:
    print("what i you play choose the number \n 1.rpsgame\n 2.guessgame\n 3.calculator\n 4.simplechat\n (or 'quit' to exit)\n")
    
    user=int(input("youchoose the num : "))

    if user==1:
        rpsplay()
    elif user==2:
        gussnumberplay()
    elif user==3:
        calculatorplay()
    elif user==4:
        simplechatbotplay()
    elif user == "quit":
        print("Thanks for playing!")
        break






        
 
    

