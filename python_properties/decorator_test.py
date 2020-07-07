class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """The docstring for the age property"""
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method ')
        if isinstance(value, int) and 0 < value < 120:
            self._age = value

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self.name

    def __str__(self):
        return f"Person [{self._name}] is {self._age} years old"


person = Person('Onyango', 34)
print(person)
print(person.age)
print(person.name)
person.age = -1
print(person.age)