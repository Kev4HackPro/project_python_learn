def run_calc(x):
    x / 0


# noinspection PyBroadException
try:
    run_calc(6)
except ZeroDivisionError as exp:
    print(exp)
    print('Number cannot be divided by zero')
except IndexError as e:
    print(e)
    print('Oops')
except FileNotFoundError:
    print('file you requested cannot be found')
except Exception as exception:
    print(exception)
    print('Oops')