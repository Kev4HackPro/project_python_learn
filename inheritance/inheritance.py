class Person:

    instance_count = 0

    @classmethod
    def increment_instance_count(cls):
        print('New instance created')
        cls.instance_count += 1

    def __init__(self, name, age):
        Person.increment_instance_count()
        self.name = name
        self.age = age

    def birthday(self):
        print(f"Happy birthday {self.name}, you were {self.age}")
        self.age += 1
        print(f"You are now {self.age} years old")

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Employee(Person):

    def __init__(self, name, age, id_no):
        super().__init__(name, age)
        self.id = id_no

    def calculate_pay(self, hours_worked):
        rate_of_pay = 7500
        if self.age >= 21:
            rate_of_pay += 2500
        return hours_worked * rate_of_pay

    def __str__(self):
        return f"{super().__str__()}. Her id_no  is ({self.id})"


class SalesPerson(Employee):

    def __init__(self, name, age, id_no, region, sales):
        super().__init__(name, age, id_no,)
        self.region = region
        self.sales = sales

    def bonus(self):
        return self.sales * 0.5

    def __str__(self):
        return f"{super().__str__()}. She sales in the region of {self.region}"


print('Person')
p = Person('Onyango', 45)
print(p)
print(p.name)
print(p.age)
p.birthday()
print('-' * 25)

print('Employee')
e = Employee('Denise', 23, 37162855)
print(e)
e.birthday()
print(e.name)
print(e.age)
print(e.id)
print('Payment of hours worked:', e.calculate_pay(40))
print('-' * 25)

print('SalesPerson')
s = SalesPerson('Rodney', 17, 456785, 'Nairobi', 145000)
print(s)
s.birthday()
print('Payment of hours worked:', s.calculate_pay(40))
print('Bonus earned: ', s.bonus())
print(f'Instances created are: {Person.instance_count}')