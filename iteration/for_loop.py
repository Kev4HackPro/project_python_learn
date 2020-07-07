print('Starting...')
for items in range(0, 10, 3):
    print(items, " ", end='')
print()
print('Done')

for i in range(0, 10):
    print('.', end='')
print()
# Break statement
print('Only print code if all iterations are completed')
num = int(input('Enter a number to check for: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, " ", end='')
print('done')
# Continue loop statement
for i in range(0, 10):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('Hey its an even number')
    print('We love even numbers')
print('Done')
