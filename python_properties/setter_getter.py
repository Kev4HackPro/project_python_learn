class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 120:
            self._age = new_age

    def get_name(self):
        return self._name

    def __str__(self):
        return f"Person[{self._name}] is {self._age}"


p = Person('John Waluke', 50)
print(p)
p.set_age(78)
print(p)
