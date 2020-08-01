# Example 1: Given a list of integers, a new list can be generated using list comprehension
list1 = [1, 2, 3, 4, 5, 6]
print('list1:', list1)

# now creating new list using list comprehension
list2 = [item + 3 for item in list1]
print('list2:', list2)
list3 = [item + 1 for item in list1 if item % 2 == 0]
print('list3:', list3)