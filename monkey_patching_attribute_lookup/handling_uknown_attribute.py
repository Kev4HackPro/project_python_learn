class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    # Method below is called if an attribute is unknown

    def __getattr__(self, attribute):
        print('__getattr__:', attribute)
        return self.my_default

    def my_default(self):
        return 'Attribute is unknown'


student = Student('Ojiambo')

res1 = student.dummy_attribute()
print('p.dummy_attribute:', res1)
