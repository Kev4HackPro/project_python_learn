class Person:
    """Use of setter and getter style methods"""
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 120:
            self._age = new_age

    age = property(get_age, set_age, doc="An age property")

    def get_name(self):
        return self._name

    name = property(get_name, doc="A name property")

    def del_name(self):
        del self.name

    name = property(get_name, fdel=del_name, doc="A name property")

    def __str__(self):
        return f"Person [{self._name}] is {self._age}"


person = Person('James', 54)
print(person)
print(person.name)
print(person.age)
person.age = 21
print(person)
