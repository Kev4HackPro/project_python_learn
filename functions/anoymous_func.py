# Lambda function to square a number

double = lambda num: num ** 2
print(double(10))
add = lambda x, y, z: x + y + z
multiply = lambda x, y: x * y
no_argument = lambda: print('No argument passed')
print(add(19, 43, 47))
print(multiply(34, 76))
no_argument()
