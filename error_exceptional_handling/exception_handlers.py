def my_function(x, y):
    print('my_function in')
    result = x / y
    print('my_function out')
    return result


print('Starting')
try:
    print('Before my_function')
    my_function(6, 0)
    print('After my_function')
except ZeroDivisionError as exp:
    print('oops')

print('Done')
