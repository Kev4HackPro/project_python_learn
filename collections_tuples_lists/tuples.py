class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return 'Person(' + self._name + ', ' + str(self._age) + ')'


# Defining a tuple
tup1 = (3, 5, 7, 8, 9)
print(tup1)
for items in tup1:
    print('', items, end='')

# the tuple() constructor function
list1 = [4, 7, 8, 9]
print('\n', tuple(list1))

# Accessing elements of a tuple
print(tup1[0])
print(tup1[1])
print(tup1[-1])
print(tup1[1:-2])  # Here we have created a new tuple from an existing one
print(tup1[0:4])  # Note that it does not print the element in the last index stated
print(tup1[::-1])  # reversing a tuple

# Tuples holding different types
tup2 = (1, 'John', Person('Phoebe', 21), True, -23.45)
print(tup2)

# iterating over tuples
fruits = ('apple', 'pear', 'banana', 'strawberry', 'lemon')
for items in fruits:
    print(items)
# tuple methods
print(len(fruits))  # finding length of  a tuple
print(fruits.index('strawberry'))  # show you the first index the item specified appears in the collection
print(fruits.count('apple'))  # counts how many times an items appears in a tuple
if 'apple' in fruits:
    print('apple is there')  # checking if an element exists
    #  or
print('apple' in fruits)  # returns a boolean value
# Nested tuples
tuple1 = (98, 67, 45, 34)
tuple2 = ('Kavita', 'Sunaina', 'Omondi')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)