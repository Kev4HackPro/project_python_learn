""" This is a test module"""
print('Hello, I am the utils module')


def printer(some_object):
    print('Printer')
    print(some_object)
    print('Done')


class Shape:
    def __init__(self, id):
        self._id = id

    def __str__(self):
        return 'Shape -' + self._id

    @property
    def id(self):
        """The docstring for id property"""
        print('In id method')
        return self._id

    @id.setter
    def id(self, value):
        print('In set age method')
        self._id = id


default_shape = Shape('Square')
print(default_shape)
