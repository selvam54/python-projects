import os
import json

todo=(input("enter the file name : "))


def start():
    while True:
        print("*************************welcome to do list***************************************")
        print("1. create")
        print("2. write")
        print("3. read") 
        print("4. delete")
        print("5. exit \n")  
        
            
        choice=input("enter the work : ")
        
        # create a file task
        

            
        
        # write task create 
        
        if choice=="2":
            task=input("write a task : ")
            with open(todo,"w") as f:
                f.write(task +"\n")
                print("task writted")
                
        # read task create
        
        if choice == "3":
            if os.path.exists(todo):
                with open(todo,"r") as f:
                    content=f.read()
                    print(content)
                    print("you are reading")
                    
        # delete task create 
        
        if choice == "4":
            if os.path.exists(todo):
                os.remove(todo)
                print("your are removing")                
        # exit task create 
        
        if choice == "5":
            print("thank for using")
            break
        

start()