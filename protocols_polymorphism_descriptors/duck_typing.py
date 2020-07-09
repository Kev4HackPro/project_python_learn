# noinspection PyMethodMayBeStatic
class Calculator:
    """Simple calculator class"""

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


class Distance:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Distance(self.value + other.value)

    def __sub__(self, other):
        return Distance(self.value - other.value)

    def __str__(self):
        return 'Distance [' + str(self.value) + ']'


calc = Calculator()
d1 = Distance(5)
d2 = Distance(6)
d3 = d1 + d2
print(calc.add(d1, d2))
print(calc.subtract(d1, d2))
print('__add__:', d3)