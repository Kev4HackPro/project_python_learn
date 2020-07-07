def convert(rate, amount):
    return rate * amount


def curry(func, rate):
    return lambda amount: func(rate, amount)


dollar_to_kes = curry(convert, 106)
print(dollar_to_kes(4500))
sterling_to_kes = curry(convert, 134)
print(sterling_to_kes(200))
kes_to_dollar = curry(convert, 0.0094)
print(kes_to_dollar(100000))
kes_to_sterling = curry(convert, 0.0075)
print(kes_to_sterling(26950))
