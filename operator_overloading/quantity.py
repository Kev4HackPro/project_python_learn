class Quantity:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __str__(self):
        return f"Quantity[{self.value}]"


print('Addition using operator overloading')
q1 = Quantity(5)
q2 = Quantity(7)
q3 = q1 + q2
print('q1=', q1, ', q2=', q2)
print('q3:', q3)
r1 = Quantity(67)
r2 = Quantity(45)
r3 = r1 - r2
print('Subtraction using operator overloading')
print('r1=', r1, ', r2=', r2)
print('r3=', r3)