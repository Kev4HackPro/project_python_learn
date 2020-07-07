class Person:
    """This class prints out name and also age
    This is done by converting the objects to strings using the __str__
     method"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is ' + str(self.age) + ' years old'

    def birthday(self):
        print('Happy birthday Cheptoo, you were', self.age)
        self.age += 1
        print('You are now', self.age)

    def calculate_pay(self, hours_worked):
        rate_of_pay = 795
        if self.age >= 21:
            rate_of_pay += 250
        return hours_worked * rate_of_pay

    def is_teenager(self):
        status = ('teenager' if self.age < 20 else 'Not a teenager')
        return status


person1 = Person('Cheptoo', 20)
person2 = Person('Adam', 17)
print(person1)
person1.birthday()
pay = person1.calculate_pay(107)
pay2 = person2.calculate_pay(107)
print(f'The pay for {person1.name} is {pay} kenya shillings')
print(f'The pay for {person2.name} is {pay2} kenya shillings')
status_quo = person1.is_teenager()
is_status_quo = person2.is_teenager()
print(f"{person1.name} of age {person1.age} is {status_quo}")
print(f"{person2.name} of age {person2.age} is a {is_status_quo}")
# intrinsic attributes
print('Class attributes')
print('-' * 25)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)
print(Person.__doc__)
print(Person.__dict__)
print('-' * 25)
print('Object attributes')
print(person1.__class__)
print(person1.__dict__)