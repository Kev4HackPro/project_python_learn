class Quantity:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __floordiv__(self, other):
        new_value = self.value // other.value
        return Quantity(new_value)

    def __pow__(self, other):
        new_value = self.value ** other.value
        return Quantity(new_value)

    def __mod__(self, other):
        new_value = self.value % other.value
        return Quantity(new_value)

    def __lshift__(self, other):
        new_value = self.value << other.value
        return Quantity(new_value)

    def __rshift__(self, other):
        new_value = self.value >> other.value
        return Quantity(new_value)

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other
        else:
            new_value = self.value * other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_value = self.value / other
        else:
            new_value = self.value / other.value
        return Quantity(new_value)

    def __str__(self):
        return f"Quantity[{self.value}]"


q1 = Quantity(10)
q2 = Quantity(5)
print('q1 * 2', q1 * 2)
print('q2 / 2', q2 / 2)
