class Person:
    """An example of class to hold person's name and age"""
    instance_count = 0  # Keeps a count of how many instances are created

    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1

    def __init__(self, name, age):
        Person.instance_count += 1
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


p1 = Person('John', 45)
print(p1)
p2 = Person('Kira', 22)
print(p2)
p3 = Person('Bien', 35)
print(p3)
p4 = Person('Trump', 73)
print(p4)
print(Person.instance_count)
Person.increment_instance_count()
