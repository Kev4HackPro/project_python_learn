class Logger(object):
    """Implements the descriptor protocol
    Can therefore be used with other classes to log the creation, access
     and update whatever attribute is applied on"""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print('__get__:', instance, 'owner:', owner,
              ', value', self.name, '=',
              str(instance.__dict__[self.name]))

    def __set__(self, instance, value):
        print('__set__:', instance, '-', self.name, '=', value)
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('__delete__', instance)

    def __set_name__(self, owner, name):
        print('__set_name__', 'owner', owner, 'setting', name)


class Cursor(object):
    # set up descriptors at class level
    x = Logger('x')
    y = Logger('y')

    # noinspection PyPep8Naming
    def __init__(self, xO, yO):
        # initialize the attributes
        # Note use of __dict__ to avoid self.x notation
        # which would invoke the descriptor behaviour
        self.__dict__['x'] = xO
        self.__dict__['y'] = yO

    def move_by(self, dx, dy):
        print('move_by', dx, ',', dy)
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return f"Point[{self.__dict__['x']}, {self.__dict__['y']}]"


cursor = Cursor(15, 25)
print('=' * 25)

print('p1:', cursor)
cursor.x = 20
cursor.y = 35
print('p1 updated', cursor)
print('p1.x', cursor.x)
print('=' * 25)

del cursor.x





