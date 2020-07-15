class Bag:
    def __init__(self):
        self.data = ['a', 'b', 'c']

    def __getitem__(self, pos):
        return self.data[pos]

    def __str__(self):
        return f'Bag({self.data})'


b = Bag()
print(b)


def get_length(self):
    return len(self.data)


# monkey patching class

Bag.__len__ = get_length
print(len(b))
# Adding new data to a class
Bag.name = 'My Bag'
print(b.name)
b.name = 'John\'s bag'
print(b.name)
b2 = Bag()
print(b2.name)
