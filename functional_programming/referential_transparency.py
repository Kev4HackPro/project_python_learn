def increment(num):
    """We say this function is referentially transparent
    if it always returns the same result for the same value"""
    return num + 1


print(increment(5))
print(increment(5))

amount = 1


def increment(num):
    """This function is not referentially transparent"""
    return num + amount


print(increment(5))
amount = 2
print(increment(5))
