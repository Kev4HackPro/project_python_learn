import random

mini = 1
maxi = 6

roll_again = 'y'.lower()
while roll_again == 'y':
    print('Rolling the dices...')
    print('The values are...')
    dice1 = random.randint(mini, maxi)
    print(dice1)
    dice2 = random.randint(mini, maxi)
    print(dice2)
    roll_again = input('Roll the dices again (y/n): ')
