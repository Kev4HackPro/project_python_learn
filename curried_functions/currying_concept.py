def multiply(a, b):
    return a * b


def multiply_by(func, num):
    return lambda y: func(num, y)


double = multiply_by(multiply, 2)
print(double(5))
triple = multiply_by(multiply, 3)
print(triple(3))
