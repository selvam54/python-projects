import json

def quiz():
    with open("file/quiz.json", "r") as read:
        data = json.load(read)
        score = 0

    for i in data:
        print("Question:", i["question"])
        for idx, opt in enumerate(i["options"], start=1):
            print(f"{idx}. {opt}")

        player = input("Enter your answer: ")

        if player == i["answer"]:
            print("Correct ✔")
            score += 1
            if score == 5:
                print("You are super! All answers correct ✔")
        else:
            print("You are wrong ✖")

        print(f"Your score is: {score}")
        
    return score
