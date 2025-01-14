import random

num_of_throws = 0
def throw_dice():
    return random.randint(1, 6)

def handle_play_game(response):
    if response not in ['y', 'n']:
        print('Invalid choice!')
        return False

    if response == 'n':
        print('Thanks for playing!')
        return False

    return True

def handle_num_of_dices(char):
    try:
        int(char)
    except ValueError:
        print('Invalid type: Please enter an integer!')
        return False
    return True

while True:
    answer = input('Roll the dice (y/n): ').lower()
    if not handle_play_game(answer):
        break

    num_of_dices = input('How many dices do you wanna roll?: ')
    if not handle_num_of_dices(num_of_dices):
        break
    num_of_dices = int(num_of_dices)

    if answer == 'y':
        num_of_throws = num_of_throws + 1

        str_results = ''
        for i in range(num_of_dices):
            if (i < num_of_dices - 1):
                str_results += (f'{str(throw_dice())},')
            else:
                str_results += str(throw_dice())

        print(f'({str_results})')
        print(f'You threw dice(s): {num_of_throws}x')
