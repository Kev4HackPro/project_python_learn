from math import *


def calculate_tax(x, function):
    result = function(x)
    return f'Tax to be paid is: {result}'


def simple_tax_calculator(amount):
    return ceil(amount * 0.3)


print(calculate_tax(80000, simple_tax_calculator))
