def logger(func):
    def inner(x, y):
        print('Calling', func.__name__, 'with', x, 'and', y)
        func(x, y)
        print('Returned from', func.__name__)

    return inner


@logger
def my_func(x, y):
    print(x, 'and', y)


my_func(4, 5)
