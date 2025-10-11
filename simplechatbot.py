import datetime
print("*******************************simple chatbot*****************************************8")
while True:
    user=input("tell any i a simple chatbot : ")
    print("you finish to tell say exit")
    if user == "hello":
        print("hi")
        print("nice to meet you")

    elif user == "how are you":
        print("I'm fine")
        print("what about you")

    elif user == "bye":
        print("goodbye")
        print("see you soon")
        break

    elif user == "thanks":
        print("you're welcome")
        print("happy to help")

    elif user == "what is your name":
        print("I am ChatBot")
        print("your virtual friend")

    elif user == "good morning":
        print("good morning!")
        print("have a great day")

    elif user == "good night":
        print("sweet dreams")
        print("sleep well")

    elif user == "who made you":
        print("I was created by programmers")
        print("to help people like you")

    elif user == "what can you do":
        print("I can chat with you")
        print("and answer simple questions")

    elif user == "what are you doing":
        print("I'm chatting with you")
        print("what about you")

    elif user == "where are you from":
        print("I'm from the internet")
        print("I live in your computer")

    elif user == "what is python":
        print("Python is a programming language")
        print("it is easy and powerful")

    elif user == "who are you":
        print("I'm a chatbot")
        print("your virtual assistant")

    elif user == "tell me a joke":
        print("Why did the computer sleep?")
        print("Because it had a hard drive!")

    elif user == "what is your favorite color":
        print("I like blue")
        print("it looks cool and calm")

    elif user == "i am bored":
        print("Let's play a game!")
        print("Try guessing my favorite number")

    elif user == "i love you":
        print("Aww, thank you!")
        print("I love chatting with you too")

    elif user == "how old are you":
        print("I'm timeless")
        print("I was created recently")

    elif user == "what is your hobby":
        print("Talking with people like you")
        print("and learning new things")

    elif user == "who is your best friend":
        print("You are!")
        print("because you talk to me")

    elif user == "do you like music":
        print("Yes, I love music")
        print("what kind do you like")

    elif user == "what time is it":
        print("I can't see the clock")
        print("but you can check your device")

    elif user == "can you dance":
        print("Haha not really")
        print("but I can make you smile")

    elif user == "what is ai":
        print("AI means Artificial Intelligence")
        print("it helps machines think like humans")
    
    elif user == "what time is it":
        print("Current time is:", datetime.now().strftime("%H:%M:%S"))
    
    elif user == "exit":
        break

    else:
        print("I don't understand that yet")
        print("try asking something else")