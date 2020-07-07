number = [45, 67, 67, 89,89, 78, 90, 67, 45, 45]
uniques = []
for items in number:
    if items not in uniques:
        uniques.append(items)
print(uniques)

for _ in range(0, 10):
    print('.', end='')
print()