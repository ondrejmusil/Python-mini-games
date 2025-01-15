import random

num_throws = 0
def throw_dice():
    return random.randint(1, 6)

def throw_dices(num_of_dices):
    return [throw_dice() for _ in range(num_of_dices)]

def display_results(results):
    print(f'({", ".join(map(str, results))})')
    print(f'You threw dice(s): {num_throws}x')

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    play_again: str = input('Roll the dice (y/n): ').lower()

    if play_again == 'n':
        print('Thanks for playing!')
        break
    elif not play_again == 'y':
        print('Please type "y" to continue or "n" to quit...')
        continue

    num_dices = input('How many dices do you want to roll?: ')
    if not is_integer(num_dices):
        print('Incorrect input. Please use number input.')
        print('New session created...')
        continue

    num_throws += 1
    player_result = throw_dices(int(num_dices))
    display_results(player_result)