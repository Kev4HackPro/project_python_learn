number = input('Number you want factorial for: ')
if number.isnumeric():
    new_number = int(number)
    if new_number == 0:
        print('factorial for zero is 1')
    else:
        factorial = 1
        for item in range(1, new_number + 1):
            factorial = factorial * item
        print(f"{number}! is {factorial}")
else:
    print('Number entered is not positive')