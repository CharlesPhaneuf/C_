import random

choices = ["Rock", "Paper", "Scissors"]

while True:
    x = random.choice(choices)
    playerinput = input("Rock, Paper or Scissors(or exit to quit): ")
    
    if playerinput.lower() == "exit":
        print("thanks for playing!")
        break

    if playerinput not in choices:
        print("Invalid input! Please choose Rock, Paper, or Scissors.")
    else:
        if x == playerinput:
            print("It's a tie! The AI chose:", x)
        elif (playerinput == "Rock" and x == "Scissors") or (playerinput == "Paper" and x == "Rock") or (playerinput == "Scissors" and x == "Paper"):
            print("You won! The AI chose:", x)
        else:
            print("You lose! The AI chose:", x)
