class InvalidAgeException(Exception):
    """Creating my own error and exception"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'InvalidAgeException (' + str(self.value) + ')'


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method (', value, ')')
        if isinstance(value, int) and 0 < value < 120:
            self._age = value

        else:
            raise InvalidAgeException(value)

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return f"{self._name} is {self._age} years old"


try:
    person = Person('Junior', 21)
    person.age = -1
except InvalidAgeException as e:
    print(e)
