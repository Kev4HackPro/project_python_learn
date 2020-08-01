import itertools

# connect two iterators together
r1 = list(itertools.chain([1, 2, 3], [2, 3, 4]))
print(r1)

# create iterator with element repeated specified number of time
r2 = list(itertools.repeat('hello', 5))
print(r2)
# create iterator with elements from first iterator starting where
# predicate function fails
values = [1, 3, 5, 7, 9, 3, 1]
r3 = list(itertools.dropwhile(lambda x: x < 5, values))
print(r3)
# create iterator with elements from supplied iterator between
# the two indexes (use 'None' for second index to go to end)
r4 = list(itertools.islice(values, 3, 6))
print(r4)

