# Import for the random number generator
import random

# Dictionary for the different difficulties
dif = {1: 'Easy', 2: 'Medium', 3: 'Hard'}
attempts = {'Easy': 10, 'Medium': 5, 'Hard': 3}
current_attempt: list = []
random_number = random.randint(1, 100)


# Introduction and rules of the game
# Set to None since we're only printing text
def intro_rules() -> None:
    # Written using \n to lessen line usage
    print('WELCOME TO NUMBER GUESSER! *made by exolection*\nI\'m thinking of a number from 1 to 100.\nCan you guess what it is?')
    print('\nChoose your difficulty:\n1. Easy (10 guesses)\n2. Medium (5 guesses)\n3. Hard (3 guesses)')


# Difficulty Selector
# Function converts the user input to 'Easy', 'Medium', or 'Hard'
def dif_select() -> str:
    # Keeps going until a valid difficulty level is chosen
    while True:
        try:
            # Prompts the user to choose a difficulty level no. from 1 to 3
            user_dif = int(input('\nSelect a difficulty level (1, 2, or 3): '))
            # If input is found in the dif dictionary
            if user_dif in dif:
                print(f'\nYou\'ve selected {dif[user_dif]} difficulty.')
                # Returns strings 'Easy', 'Medium', or 'Hard' as results of the function
                return dif[user_dif]
            # If chosen difficulty integer isn't found in the dif dictionary
            else:
                print('\nNot a valid option!')
        # No exception error, but replaces it with 'Not a valid difficulty level!'
        except ValueError:
            print('\nNot a valid option!')


# Attempt checker
# Function determines how many tries the user has based on the dif_select() string and the attempts dictionary
def attempt_check() -> int:
    tries = attempts[dif_select()]
    current_attempt.append(tries)
    return tries

# Main Game
def main(number: int, attempt: int = 1):
    tries: int = int(current_attempt[0])
    if attempt > tries:
        print('Game Over! The correct number was:', number)
        return None

    guess: int = int(input(f'\nAttempt {attempt}/{tries}. Pick a number: '))

    try:
        guess
    except ValueError:
        print('Please input a valid number.\n')
        return main(number, attempt)
    if guess < 1 or guess > 100:
        print('Please input a valid number between 1 and 100!\n')
        return main(number, attempt)

    guess_check = lambda x, y: 'correct' if x == y else (
        'low' if x < y else 'high'
    )

    result = guess_check(guess, number)

    if result == 'correct':
        print('Wow! You guessed my number correctly.\nMy number is', number)
        return None
    elif result == 'low':
        print('Incorrect! Try a higher number!\n')
    else:
        print('Incorrect! Try a lower number!\n')

    main(number, attempt + 1)
    return None

intro_rules()
attempt_check()
main(random_number)
