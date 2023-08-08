import random

options = ["rock", "paper", "scissors"]

rules = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock"
}

player_score = 0
computer_score = 0

rounds = 3

for i in range(rounds):
    print(f"round {i+1}")

    player_choice = input("Choose rock, paper, scissors ").lower()

    while player_choice not in options:
        print("Invalid Choice")
        player_choice = input("Choose rock, paper, scissors ").lower()

    computer_choice = random.choice(options)

    print(f"The Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("its a tie")

    elif rules[player_choice] == computer_choice:
        print("You Win")
        player_score += 1
    else:
        print("You Lose")
        computer_score += 1

    print(f"Your score is {player_score}")
    print(f"Computer score is {computer_score}")
    print()

print("The Game is Over")

if player_score > computer_score:
    print("You WIN the game")
elif computer_score > player_score:
    print("You lose the game")
else:
    print("Its a aaa a big tie")

print("HIIII")

print("NEW")

f