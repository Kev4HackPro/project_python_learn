"""The code here asks user to enter a number. The code checks if it is in the range between 0 and 6.
The if that follows states that when number entered matches number in range, break(end the code there) e.g 
In the case we enter 3, the code will print 0, 1, 2. As you know as range works, it usually does not print the last number
The else statement in our for loop is to run, if all numbers in the range are have been iterated. (e.g. In our case it was 6)
"""
print('Only print code if all iterations completed')
num = int(input('Enter a number to check for: ')) 
for i in range(0, 6):
    if i == num:
        break
    print(i, " ", end='')
else:
    print()
    print('All iterations successful')