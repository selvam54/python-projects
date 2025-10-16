def simplechatbotplay():
    import datetime
    print("******************************* Simple Chatbot *****************************************")

    while True:
        user = input("Tell me something, I am a simple chatbot: ")
        print("You can say 'exit' to finish")

        if user == "hello":
            print("Hi")
            print("Nice to meet you")

        elif user == "how are you":
            print("I'm fine")
            print("What about you")

        elif user == "bye":
            print("Goodbye")
            print("See you soon")
            break

        elif user == "thanks":
            print("You're welcome")
            print("Happy to help")

        elif user == "what is your name":
            print("I am ChatBot")
            print("Your virtual friend")

        elif user == "good morning":
            print("Good morning!")
            print("Have a great day")

        elif user == "good night":
            print("Sweet dreams")
            print("Sleep well")

        elif user == "who made you":
            print("I was created by programmers")
            print("To help people like you")

        elif user == "what can you do":
            print("I can chat with you")
            print("And answer simple questions")

        elif user == "what are you doing":
            print("I'm chatting with you")
            print("What about you")

        elif user == "where are you from":
            print("I'm from the internet")
            print("I live in your computer")

        elif user == "what is python":
            print("Python is a programming language")
            print("It is easy and powerful")

        elif user == "who are you":
            print("I'm a chatbot")
            print("Your virtual assistant")

        elif user == "tell me a joke":
            print("Why did the computer sleep?")
            print("Because it had a hard drive!")

        elif user == "what is your favorite color":
            print("I like blue")
            print("It looks cool and calm")

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
            print("And learning new things")

        elif user == "who is your best friend":
            print("You are!")
            print("Because you talk to me")

        elif user == "do you like music":
            print("Yes, I love music")
            print("What kind do you like")

        elif user == "what time is it":
            print("I can't see the clock")
            print("But you can check your device")

        elif user == "can you dance":
            print("Haha not really")
            print("But I can make you smile")

        elif user == "what is ai":
            print("AI means Artificial Intelligence")
            print("It helps machines think like humans")

        elif user == "current time":
            print("Current time is:", datetime.datetime.now().strftime("%H:%M:%S"))

        elif user == "exit":
            break

        else:
            print("I don't understand that yet")
            print("Try asking something else")

