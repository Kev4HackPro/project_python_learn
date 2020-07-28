# defining a set
fruit_basket = {'apple', 'oranges', 'bananas', 'peaches', 'guavas'}
for fruits in fruit_basket:
    print('', fruits, end='\t \n')

# the set() constructor definition
set1 = (45, 67, 56, 78, 90)
print(set(set1))
# set methods
print('apple' in fruit_basket)  # checking elements in a set
fruit_basket.add('apricot')  # adding new element to a set
print(fruit_basket)
fruit_basket.update(['pears', 'mangoes', 'papaws', 'avocado'])  # adding more than one element to a set
# note use of lists inside the .update()
print(fruit_basket)
print('No of fruits in the basket are:', len(fruit_basket))
# obtaining minimum and maximum values in a set
numbers = {10, 56, 78, 67, 45}
print(max(numbers))
print(min(numbers))
fruit_basket.remove('apricot')  # generates an error if item is not in set
print(fruit_basket)
fruit_basket.discard('apple')  # removing an item from a set

# NESTING SETS
st1 = {(45, 67, 78, 89)}  # this is only possible with immutable objects, therefore it cannot hold a list or set
print(st1)
# to solve above problem, we therefore use frozen sets
s2 = {frozenset([45, 76, 87, 98])}
print(s2)
s3 = {frozenset([345, 678, 908, 456])}
print(s3)

# SET OPERATIONS
junk1 = {'kebab', 'fries', 'burger', 'fried chicken'}
junk2 = {'nyama choma', 'bhajia', 'sausages', 'hot dogs', 'fries'}
print('Union:', junk1 | junk2)  # combine two sets together
print('Intersection:', junk1 & junk2)  # what is common between the two sets
print('Difference:', junk1 - junk2)  # what is in set 2 but not in set 1
print('Symmetric difference:', junk1 ^ junk2)  # what is unique in set1 and set2
# the operations as methods
print(junk1.intersection(junk2))
print(junk1.difference(junk2))
print(junk1.union(junk2))
print(junk1.symmetric_difference(junk2))
fruit_basket.pop()
print(fruit_basket)
fruit_basket.update(['melons'])
print(fruit_basket)