def apply(x, function):
    """Receives functions below as parameters"""
    result = function(x)
    return result


def multiply(y):
    return y * 10.0


def square(num):
    return num * num


def multiply_by_two(num):
    return num * 2


print(apply(19, multiply))
print(apply(7, square))
print(apply(78, multiply_by_two))
