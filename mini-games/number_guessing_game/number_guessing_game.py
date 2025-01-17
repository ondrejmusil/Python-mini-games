import random

# Number to be guessed
min: int = int(input('Please enter a min number: '))
max: int = int(input('Please enter a max number: '))
max_num_of_guesses: int = int(input('How many guesses would you like to guess?: '))

if max_num_of_guesses < 1:
    print('Please enter a number greater than 1.')
    raise ValueError('Number of guesses cannot be less than 1.')

if max < min or min > max:
    raise ValueError('Max value must be lower than min value!')

actual_number_of_guesses = 0
number = random.randint(min, max)

#Best score
with open('best_score.txt', 'r') as file:
    content = file.read()
best_score: int = int(content)

def is_integer(input):
    try:
        int(input)
    except ValueError:
        print('Invalid type: Please enter an integer!')
        return False

    return True

def is_within_range(min, max, input):
    if int(input) not in range(min, max + 1):
        print(f'Error: You must enter a number in range {min} to {max}. Please try again!')
        return False

    return True

def evaluate_guess(guess, number, best_score):
    if guess > number:
        print('Too high!')
        return False
    elif guess < number:
        print('Too low!')
        return False
    else:
        print(f'Congratulations!! You guessed the number: {guess}')
        evaluate_score(best_score)
        return True

def evaluate_score(best_score):
    if best_score == 0:
        best_score = actual_number_of_guesses

        with open('best_score.txt', 'w') as file:
            file.write(str(best_score))

        print(f'Your new best score is {best_score}')
    elif best_score > actual_number_of_guesses:
        best_score = actual_number_of_guesses

        with open('best_score.txt', 'w') as file:
            file.write(str(best_score))

        print(f'New best score is {best_score}')
    else:
        print(f'The best score is: {best_score}')


# The GAME
while True:
    if actual_number_of_guesses < max_num_of_guesses:
        guess = int(input(f'Please enter a number between {min} and {max}: '))
        actual_number_of_guesses += 1

        if not is_within_range(min, max, number):
            break

        if evaluate_guess(guess, number, best_score):
            break
        else:
            continue
    else:
        print(f'Game over! You ran out of guesses. The number was {number}.')
        print(f'The best score is: {best_score}')
        break


