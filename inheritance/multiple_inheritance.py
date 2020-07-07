class Car:

    def move(self):
        print('Car - move()')


class Toy:

    def move(self):
        print('Toy  - move()')


class ToyCar(Toy, Car):
    """A Toy car"""


tc = ToyCar()
tc.move()
