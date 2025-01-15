import random

mapping = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

winning_combinations = {
    'r': 's',
    'p': 'r',
    's': 'p'
}

options = ['r', 'p', 's']

def generate_choice():
    return random.choice(options)

def check_input(input):
    if input not in options:
        print("Invalid input")
        return False
    return input

def determine_winner(playerChoice, computerChoice):
    if playerChoice not in options:
        print("Invalid input")

    if playerChoice == computerChoice:
        print("It's a tie!")
    elif winning_combinations[playerChoice] == computerChoice:
        print("You win!")
    else:
        print("You lose!")


while True:
    player_choice = check_input(input('Rock, paper or scissors? (r/p/s): ').lower())
    if not player_choice:
        continue

    computer_choice = generate_choice()

    print(f'You chose: {mapping[player_choice]}')
    print(f'Computer chose: {mapping[computer_choice]}')

    determine_winner(player_choice, computer_choice)




