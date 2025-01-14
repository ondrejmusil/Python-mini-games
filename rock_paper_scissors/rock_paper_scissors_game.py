import random

from dice_rolling_game.dice_rolling_game import num_of_throws

mapping = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

def generate_choice():
    return random.choice(["r", "p", "s"])

def check_input(input):
    if input not in ["r", "p", "s"]:
        print("Invalid input")
        return False
    return input

while True:


    player_choice = check_input(input('Rock, paper or scissors? (r/p/s): ').lower())
    if not player_choice:
        continue

    computer_choice = generate_choice()

    print(f'You chose: {mapping[player_choice]}')
    print(f'Computer chose: {mapping[computer_choice]}')

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "p":
        if computer_choice == "s":
            print("You lose!")
        elif computer_choice == "r":
            print("You win!")
    elif player_choice == "s":
        if computer_choice == "r":
            print("You lose!")
        elif computer_choice == "p":
            print("You win!")
    elif player_choice == "r":
        if computer_choice == "p":
            print("You lose!")
        elif computer_choice == "s":
            print("You win!")
    else:
        print('Unhandled condition!')




