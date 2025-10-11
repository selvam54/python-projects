import json
print("****************************Quiz Game**********************************")

#read the json question file

with open("quiz.json","r") as read:
    #json in list
    data=json.load(read)
    score=0
        
for i in data:
    print("question ",i["question"])
    for idx, opt in enumerate(i["options"], start=1):
        print(f"{idx}. {opt}")

    player=input("enter your answer : ")
    
    if player==i["answer"]:
        print("correct \u2714")
        score+=1
        if score==5:
            print("you are super your answer all correct \u2714")
    else:
        print("you are wrong \u2716")
    print(f"your score is : {score}")
        
    
        
    
    
    
    

