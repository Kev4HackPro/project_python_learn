class Quantity:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other
        else:
            new_value =self.value * other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        new_value = self.value / other.value
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

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

    def __str__(self):
        return f"Quantity[{self.value}]"


q1 = Quantity(5)
q2 = Quantity(10)
print('q1=', q1, ', q2=', q2)
q3 = q1 * q2
print('q3=', q3)
print('q1 < q2: ', q1 < q2)
print('q3 > q2: ', q3 > q2)
print('q3 == q1: ', q3 == q1)