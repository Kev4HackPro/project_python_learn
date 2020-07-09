def function_bang():
    print('function bang in')
    raise ValueError('Yeah, i just raised an exception')
    # noinspection PyUnreachableCode
    print('function_bang')


try:
    function_bang()
except ValueError as ve:
    print(ve)
    print('oops')

