class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __add__(self, other):
        new_distance = self.distance + other.distance
        return Distance(new_distance)

    def __sub__(self, other):
        new_distance = self.distance - other.distance
        return Distance(new_distance)

    def __mul__(self, other):
        if isinstance(other, int):
            new_distance = self.distance * other
        else:
            new_distance = self.distance * other.distance
        return Distance(new_distance)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_distance = self.distance / other
        else:
            new_distance = self.distance * other.distance

        return Distance(new_distance)

    def __floordiv__(self, other):
        if isinstance(other, int):
            new_distance = self.distance // other
        else:
            new_distance = self.distance // other.distance
        return Distance(new_distance)

    def __str__(self):
        return f"Distance [{self.distance}]"


d1 = Distance(6)
d2 = Distance(3)
print(d1 + d2)
print(d1 - d2)
print(d1 / 2)
print(d2 // 2)
print(d2 * 2)
