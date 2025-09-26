#calculator operators

#loop
while True:
    
    #quit section 
    #if  num1 == "quit":
        #break 
    
    def calculator(num1,num2):
        if user == "+":
            return num1 + num2
        elif user == "-":
            return num1 - num2
        elif user == "*":
            return num1 * num2
        elif user == "%":
            return num1 % num2
    
#user input
    
    num1=int(input("enter the number : "))
    user=input("addition + \n subraction - \n multiplication * \n divide % \n what you choose : ")
    num2=int(input("enter the number : "))
    
    
    print(f"{num1} {user} {num2} answer is : {calculator(num1,num2)}")
