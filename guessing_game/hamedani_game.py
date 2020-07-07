import random
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Hey, guess a number between 1 to 10: '))
    guess_count += 1
    if guess == secret_number:
        print('Hurray you won')


