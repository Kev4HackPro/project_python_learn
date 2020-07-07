def increment(num):
    return num + 1


def reset_increment():
    global increment
    addition = 50
    increment = lambda num: num + addition


print(increment(10))
reset_increment()
print(increment(70))