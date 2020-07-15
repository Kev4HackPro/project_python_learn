# Definition of a simple logger decorator function


def logger(func):
    def inner():
        print('Calling', func.__name__)
        func()
        print('Called', func.__name__)

    #     inner function is not executed

    return inner  # reference to inner function returned under logger(


# using decorators

@logger
def target():
    print('In target function')


target()

# functions with parameters


@logger
def my_func(x, y):
    print(x, y)

my_func(4, 5)

