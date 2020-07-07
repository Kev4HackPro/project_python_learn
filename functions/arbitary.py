def greeter(*args):
    for names in args:
        print('Welcome', names)


greeter('Kavita', 'Nzara', 'Sunaina', 'Ian', 'Luka' )


# Positional and keyword arguments
def my_function(*args, **kwargs):
    for arg in args:
        print('arg:', arg)
    for key in kwargs.keys():
        print('key:', key, 'has value:', kwargs[key])


my_function('Kavita', 'Sunaina', son='Ahmed', daughter='fatma')
print('-' * 50)
my_function('Omondi', 'Atieno', first_daughter='Awiti', second_daughter='Akoth', son='Owino')


def number(**kwargs):
    for key in kwargs.keys():
        print('arg:', key, 'has value', kwargs[key])


number(a=1, c=9, b=5)
