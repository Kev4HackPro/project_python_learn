import random

print('Welcome to the number guessing game')
print('.' * 40)
secret_number = random.randint(1, 50)
guess_count = 0
guess_limit = 4
game_continue = 'y'.lower()
while guess_count < guess_limit:
    guess = int(input('Enter guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Hurray you won, congratulations')
        print(f'You took {guess_count} tries  to complete the game')
        break
    elif guess < secret_number:
        print('Secret number is higher')
    elif guess > secret_number:
        print('Secret number is lower ')
else:
    print(f"You lost the game, the secret number was {secret_number}")
    print('Game Over!!!!')
