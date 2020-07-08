class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __add__(self, other):
        new_value = self.distance + other.distance
        return Distance(new_value)

    def __sub__(self, other):
        new_value = self.distance - other.distance
        return Distance(new_value)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_value = self.distance / other
        else:
            new_value = self.distance / other.distance
        return Distance(new_value)

    def __floordiv__(self, other):
        if isinstance(other, int):
            new_value = self.distance // other
        else:
            new_value = self.distance // other.distance
        return Distance(new_value)

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.distance * other
        else:
            new_value = self.distance * other.distance
        return Distance(new_value)

    def __str__(self):
        return f"Distance[{self.distance}]"


d1 = Distance(6)
d2 = Distance(7)
print(d1 + d2)
print(d1 - d2)
print(d1 / d2)
print(d1 // d2)
print(d1 * d2)
