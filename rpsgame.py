import random

def rpsplay():
    print("***************************** Welcome To Rock Paper Scissor Game *****************************")

    # Choices and scores
    choices = ["rock", "paper", "scissor"]
    player_score = 0
    computer_score = 0

    while True:
        # Player choice
        playerchoice = input(f"\nROCK ✊\nPAPER ✋\nSCISSOR ✌\nEnter your choice (or 'quit' to exit): ").lower()

        # Quit section
        if playerchoice == "quit":
            print("Thanks for playing!")
            break

        # Invalid input check
        if playerchoice not in choices:
            print("Invalid input! Please choose rock, paper, or scissor.")
            continue

        # Computer choice
        computerchoice = random.choice(choices)
        print("Computer choice is:", computerchoice)

        # Comparison
        if playerchoice == computerchoice:
            print("Tie game!")
        elif (playerchoice == "rock" and computerchoice == "scissor") or \
             (playerchoice == "paper" and computerchoice == "rock") or \
             (playerchoice == "scissor" and computerchoice == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Display scores
        print("Your score:", player_score, "\nComputer score:", computer_score)

# Run the game
