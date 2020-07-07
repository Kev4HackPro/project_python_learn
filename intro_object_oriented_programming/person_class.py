class Person:

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def behaviour(self, profession, organization):
        return f"{self.name} is a {profession} at {organization} at only {self.age} years of age"
    
    def status(self, condition):
        return f"{self.name} is {condition} to {person1.name} for 6 months now"


person1 = Person('Kelvin Kavita', 'Kitisuru, 4th street', 23)
p = person1
person2 = Person('Anita Kavita', 'Kitisuru, 4th street', 23)
print(person1.name)
print(person1.address)
print(person1.age)
print(person1.behaviour('Senior Actuarial Consultant', 'PwC'))
print(person2.status('engaged'))
print(f'{id(person1)}')
print(f'{id(p)}')
print(f'{id(person2)}')
print(person1)
person2.age = 22
person2.name = 'Emiliana Robinson'
print(person2.name)
print(person2.age)