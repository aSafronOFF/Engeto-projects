"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Antonin Safronov
email: antonin.safronov@gmail.com
discord: TonyEntony#4102
"""
import random

separator =  '-' * 40

def bulls_and_cows_main():
    '''
    Main function for Bulls and Cows game.
    '''
    create_welcome_message()
    guessed_number = create_guessed_number()

    guess_count = 0

    while True:
        guess = get_user_guess()
        guess_count += 1 

        print(separator)

        if guess == 'quit':
            break

        if check_guess(guess, guessed_number, guess_count):
            break

def get_user_guess():
    '''
    Gets the user's guess and validates it.
    '''
    while True:
        guess = input('Enter a number: ')
        if guess == 'quit':
            break
        elif guess[0] == '0':
            print("Your number cannot start with 0.")
        elif not guess.isdigit():
            print("Your guess must be a whole number and cannot include " 
                  "any other symbols.")
        elif not are_digits_unique(guess):
            print("Digits in your number must be unique.")
        else:
            return guess


def check_guess(guess, guessed_number, guess_count):
    '''
    Checks the user's guess and prints the result.
    '''
    if guess == guessed_number:
        print(f"Correct! You've guessed the right number "
              f"in {guess_count} guesses!")
        return True
    else:
        check_length(input_number=guess, expected_number=guessed_number)
        bulls_and_cows_count(guess=guess, guessed_number=guessed_number)
        return False


def create_welcome_message():
    '''
    Creates the welcome message.
    '''
    welcome = "Hello there! Are you ready to play with the Bulls & Cows?"

    separator =  '-' * len(welcome)

    info = "I've created a random 4 digit number for you.\nYou can start playing!"

    print(separator, welcome, separator, info, separator, sep='\n')


def create_welcome_message():
    '''
    Creates the welcome message.
    '''
    welcome = "Hello there! Are you ready to play with the Bulls & Cows?"

    separator =  '-' * len(welcome)

    info = "I've created a random 4 digit number for you.\nYou can start playing!"

    print(separator, welcome, separator, info, separator, sep='\n')


def create_guessed_number(digits_count=4):
    '''
    Creates random number with the length based on digits count parameter.
    Cannot start with 0 and digits must be unique.

    Parameters:
    digits_count (int): Number of digits in the guessed number. Default is 4.

    Returns:
    str: A string representing the randomly generated guessed number.
    '''
    first_digit = random.randint(1, 9)

    remaining_digits = list(range(10))
    remaining_digits.remove(first_digit)

    unique_remaining_number = random.sample(remaining_digits, digits_count-1)
    
    number = str(first_digit) + ''.join(map(str, unique_remaining_number))

    return number

def are_digits_unique(number):
    '''
    Checks that number has unique digits.

    Parameters:
    number (int): The number to check for uniqueness.

    Returns:
    bool: True if the digits in the number are unique, False otherwise.
    '''
    number_str = str(number)

    unique_digits = set()

    for digit in number_str:
        if digit in unique_digits:
            return False
        else:
            unique_digits.add(digit)
    return True

def check_length(input_number, expected_number):
    '''
    Checks length of the number entered by user.

    Parameters:
    input_number (str): The number entered by the user.
    expected_number (str): The expected number to be guessed.

    Returns:
    None: Prints a message if the length of the input number doesn't match the expected number.
    '''
    if len(input_number) == len(expected_number):
        pass
    elif len(input_number) < len(expected_number):
        print("Your guess is too short, guessed number has "
              f"{len(expected_number)} digits.")
        print(separator)
    elif len(input_number) > len(expected_number):
        print("Your guess is too long, guessed number has "
              f"{len(expected_number)} digits.")
        print(separator)

def bulls_and_cows_count(guess, guessed_number):
    '''
    Counts the number of bulls and cows in the guessed number based on the guess.

    Parameters:
    guess (int): The guess made by the player.
    guessed_number (int): The number to be guessed.

    Returns:
    None: Prints the number of bulls and cows in the guess compared to the guessed number.
    '''
    guess_str = str(guess)
    guessed_number_str = str(guessed_number)

    bulls = 0
    cows = 0
    position = 0
    
    for number in guess_str:
        if number in guessed_number_str:
            if number == guessed_number_str[position]:
                position += 1
                bulls += 1
            else:
                position += 1
                cows += 1

    bulls_text = "bull" if bulls == 1 else "bulls"
    cows_text = "cow" if cows == 1 else "cows"
    
    print(f'{bulls} {bulls_text}, {cows} {cows_text}')

bulls_and_cows_main()