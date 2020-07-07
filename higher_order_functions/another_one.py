def make_function():
    def adder(x, y):
        return x + y

    return adder


f1 = make_function()
print(f1(5, 10))
print(f1(10, 27))
print(f1(2, 3))