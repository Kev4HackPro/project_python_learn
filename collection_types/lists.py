# Defining a list

list1 = ['Paul', 'Kenyatta', 'XI JIN PING']
for names in list1:
    print('', names, end='\t\n')

# Nested lists
l1 = [3, 45, 78, 90]
l2 = ['Pombe', 'Onyango', 'Yussuf']
l3 = ['nested', l1, l2, 'end of nested list']
print(l3)
# List() constructor function
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(list(vowel_tuple))

# Accessing elements from a list
names = ['Bruce', 'Luther', 'Barry', 'Allen']
print(names[0])
print(names[3])
print(names[1:-1])
print(names[::-1])
print(names[:3])
print(names[0:])
print(names[:])

# List methods
# N/B: the extend () and += here strictly take an iterable e.g list, set, dictionary or tuple
names.append('Wick')  # adding an element to a list
print(names)
names.extend(['Albert', 'PennyWorth'])  # adding a list to another list
print(names)
names += ['Jidenna', 'Nasty C']  # adding a existing  list to another list
print(names)
names.insert(3, 'Paloma')
print(names)
list1 = [3, 567, 78, 56]
list2 = [345, 567, 4567]
list3 = list1 + list2  # list concatenation
names.remove('PennyWorth')  # removes item stated from the list
print(names)
names.pop()  # removes the last item on the list unless an index is stated
print(names)
del names[2] # deletes item in the index stated and if no index is stated it deletes the whole list
print(names)
print('Bruce' in names)
names.reverse()
print(names)  # reverses the list
names.sort()
print(names)  # sorts the list, in this example it sorts the list alphabetically
names.copy()  # copies original list
print(names)
print(names.index('Jidenna'))  # returns index of the element specified
names.clear()
print(names)  # returns an empty list