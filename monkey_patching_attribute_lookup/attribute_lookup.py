class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


student = Student('John')
# Class attribute dictionary
print('Student.__dict__:', Student.__dict__)
# Instance / Object dictionary
print('student.__dict__', student.__dict__)

print('Student.count:', Student.count)  # class lookup
print('student.name:', student.name)  # instance lookup
print('student.count:', student.count)  # lookup finds class attribute
