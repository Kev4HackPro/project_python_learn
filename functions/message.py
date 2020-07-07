def message(msg):
    return f'Hello {msg}'


print(message('Mr Actuary the programmer'))
print(message('Good evening'))
print(message('Have a nice day'))


def square(n):
    return n * n


result = square(5)
print(result)
print(square(10))
if square(10) > 25:
    print('We did it')

