class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """Age property"""
        print('In age method')
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 120:
            self._age = new_age

    @property
    def name(self):
        print('In name method')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    def __str__(self):
        return f"Person[{self._name}] is {self._age}"


p = Person('Kamau Karanja', 45)
print(p)
p.age = 78
print(p)

