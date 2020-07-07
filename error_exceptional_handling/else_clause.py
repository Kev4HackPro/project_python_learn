def my_function(x, y):
    print('My function in')
    result = x / y
    print('My function out')
    return result


print('starting...')

try:
    my_function(6, 6)
except ZeroDivisionError as exp:
    print(exp)
else:
    print('Everything worked ok')
finally:
    print('Always runs')

print('Done')
