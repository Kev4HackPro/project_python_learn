"""The intention of this program is to identify even numbers between 0-10(but remember
range function prints from 0-9, 10 will be excluded. So the for loop states for numbers between
0-10, print the numbers and if we find the number is odd(remainder is 1), we continue to the next number
which will be even and attach the message 'Hey its an even number, mbago loves even numbers 
The program will terminate once all the numbers btwn 0-10 have been iterated through)
"""
for i in range(0, 10):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('Hey its an even number')
    print('Mbago loves even numbers')
print('Done')
