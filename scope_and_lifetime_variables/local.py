def my_function():

    a_variable = 100  # Local variable
    print(a_variable)


a_variable = 56  # Global
my_function()
print(a_variable)

maxi = 35


def print_max():
    global maxi
    maxi = maxi + 10
    print(maxi)


print_max()
print(maxi)
