def greet_user(name, message):  # parameter name and message
    return f'Welcome {name}, {message}'


print(greet_user('Kelvin Kavita', 'hope you like coding.'))  # Argument passed


# Default parameter values
def greet_user(name, message='you will become a very successful actuary one day'):
    return f'Welcome {name}, {message}'


print(greet_user('Kelvin Kavita'))


# Named arguments
def greeter(name,
            prompt='Welcome',
            title='(FIA, CERA FeASK).',
            message='Welcome aboard to PwC UK'):
    print(prompt, name, title, message)


greeter(name='Kelvin Kavita', message='You are the new chief actuary at Milliman')


def greeter(name,
            prompt='Welcome',
            title='congratulations you have been selected for PwC graduate program',
            message='Welcome aboard to PwC Kenya'):
    print(prompt, name, title, message)


greeter(name='Kelvin Kavita')
