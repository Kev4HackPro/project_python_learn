def function_bang():
    print('function bang in')
    raise ValueError('Bang')
    # noinspection PyUnreachableCode
    print('function_bang')


try:
    function_bang()
except ValueError:
    print('oops')
    
