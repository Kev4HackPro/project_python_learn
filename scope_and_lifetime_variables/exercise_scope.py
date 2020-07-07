from random import randint
import time

secret_number = randint(1, 10)
guess_count = 1


def welcome_message():
    print('Welcome to the number guessing game...')
    time.sleep(2)
    print('Designed by Kelvin Kavita')
    time.sleep(2)
    print('In collaboration with Python for beginners book')
    time.sleep(2)
    print('Starting the game...')
    time.sleep(3)


def game_over_message():
    print('Game over!!')


def get_user_input(prompt):
    invalid_input = True
    while invalid_input:
        print(prompt)
        user_input = input()
        if not user_input.isdigit():
            print('Number entered must be a positive number')
        else:
            user_input_int = int(user_input)
            if user_input_int < 1 or user_input_int > 10:
                print('Number entered must be between range 1 and 10')
            else:
                invalid_input = False
    # noinspection PyUnboundLocalVariable
    return user_input_int


def play_game():
    global guess_count
    guess = get_user_input('Please enter a number between 1 and 10: ')
    while secret_number != guess:
        print('Sorry, wrong number entered')
        if guess_count == 4:
            break
        elif secret_number > guess:
            print('Secret number is higher than your guess')
        elif secret_number < guess:
            print('Secret number is lower than your guess')

        guess = int(input('Guess again: '))
        guess_count += 1
    return guess


def check_win(guess):
    if guess == secret_number:
        print('Hurray you win!!!')
    else:
        print('You lose mate, Sorry')
        print(f'Number to guess was {secret_number}')


welcome_message()
guess_game = play_game()
check_win(guess_game)
game_over_message()