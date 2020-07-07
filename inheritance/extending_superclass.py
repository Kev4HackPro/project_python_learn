class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f" {self.name} is {self.age} years old"


class Employee(Person):

    def __init__(self, name, age, id_no):
        super().__init__(name, age)
        self.id_no = id_no

    def __str__(self):
        return f"{super().__str__()} id_no({self.id_no})"


p = Person('Kavita', 20)
print(p)
e = Employee('Donovan', 35, 34567890)
print(e)
