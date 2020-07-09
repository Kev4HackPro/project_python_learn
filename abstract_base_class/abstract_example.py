from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, id):
        self._id = id

    @abstractmethod
    def display(self): pass

    @property
    @abstractmethod
    def id(self): pass


class Circle(Shape):
    def __init__(self, id):
        super().__init__(id)

    def display(self):
        print('Circle:', self._id)

    @property
    def id(self):
        """The id property"""
        return self._id


c = Circle("circle1")
print(c.id)
c.display()