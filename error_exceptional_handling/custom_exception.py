class InvalidAgeException(Exception):
    """"Valid ages must be between 0 and 120"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Age entered must be between 0 and 120, you entered {self.value}"


class Person:
    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('New instance created')
        cls.instance_count += 1

    def __init__(self, name, age):
        Person.increment_instance_count()
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 120:
            self._age = new_age
        else:
            raise InvalidAgeException(new_age)

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return f"Person[{self._name}] is {self._age}"


try:
    p = Person('James Kariuki', 67)
    print(p)
    p.age = 30
    print(p)
except InvalidAgeException as e:
    print(e)
