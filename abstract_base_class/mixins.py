from abc import ABCMeta


class PrinterMixin(metaclass=ABCMeta):
    def print_me(self):
        print(self)


class IDPrinterMixin(metaclass=ABCMeta):
    def print_id(self):
        print(self.id)


class Person(object):
    def __init__(self, name):
        self.name = name


class Employee(Person, PrinterMixin, IDPrinterMixin):
    def __init__(self, name, age, id):
        super().__init__(name)
        self.age = age
        self.id = id

    def __str__(self):
        return f"Employee({self.id}) {self.name}, {self.age}"


e = Employee('Megan', 21, 'MS123')
e.print_me()
e.print_id()



