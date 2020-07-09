from abc import ABCMeta


class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy birthday')


class Employee(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def birthday(self):
        print('Its your birthday')


def main():
    # noinspection PyUnresolvedReferences
    Person.register(Employee)
    print(issubclass(Employee, Person))
    e = Employee('Megan', 21, 'MS123')
    print(isinstance(e, Person))


if __name__ == '__main__':
    main()
