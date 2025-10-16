import random

def gussnumberplay():
    print("******************************** Guess Number Game *********************************************")
    score = 0

    # Player choice loop
    while True:
        playerchoice = input("\nEnter a number between 1 and 5 (or 'quit' to exit): ")

        # Quit condition
        if playerchoice.lower() == "quit":
            print("Thanks for playing!")
            break

        # Validate input
        if playerchoice not in ["1", "2", "3", "4", "5"]:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        # Computer choice
        computerchoice = random.choice(["1", "2", "3", "4", "5"])
        print("The computer choice is:", computerchoice)

        # Comparison
        if playerchoice == computerchoice:
            print("You correctly guessed the number!")
            score += 1
        else:
            print("You lose!")

        # Display score
        print("Your score is:", score)

# Run the game

