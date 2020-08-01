import collections

# Using the Counter type to efficiently hold elements of the same type
# efficient because it only holds one copy of each element but keeps
# a count  of the number of times that element has been added to the collection

fruit = collections.Counter(['apple', 'orange',
                             'orange', 'orange', 'apple', 'pear', 'orange', 'apple'])
print(fruit)
print(fruit['apple'])
# to generate the most common fruit in the collection we can use the following
print('fruit.most_common(1)', fruit.most_common(1))
fruit1 = collections.Counter(['apple', 'orange', 'pear', 'orange'])
fruit2 = collections.Counter(['banana', 'apple', 'apple'])
print('fruit1:', fruit1)
print('fruit2:', fruit2)
print('Addition:', fruit1 + fruit2)
print('Subtraction:', fruit1 - fruit2)
print('Union:', fruit1 | fruit2)  # Union (max(fruit[n], fruit2[n]
print('Intersection:', fruit1 & fruit2)  # intersection (min(fruit1[n], fruit2[n])
# testing to see if an item is present in a Counter object that has been created
print('apple' in fruit1)
# adding items to a counter object
fruit['apple'] = 1  # initializes number of apples
fruit['apple'] += 1 # adds one to the number of apples
fruit['apple'] -= 1 # subtracts 1 from the number of apples
print(fruit)
