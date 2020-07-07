import time
print('Simple Calculator App')
print('By Kelvin Kavita, future actuary')
print('Starting...')
time.sleep(3)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def integer_division(x, y):
    return x // y


def modulus(x, y):
    return x % y


def exponent(x, y):
    return x ** y


def check_if_user_has_finished():
    ok_to_finish = True
    user_input_accepted = False
    while not user_input_accepted:
        user_input = input('Do you want to finish(y/n): ').lower()
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
            user_input_accepted = True
        else:
            print('Response must be (y/n), please try again')
    return ok_to_finish


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu Options are: ')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('\t5. Integer Division')
        print('\t6. Modulus(Remainder)')
        print('\t7. Exponent(power)')
        print('-' * 45)
        user_selection = input('Please make a selection from the menu choice: ')
        if user_selection in ('1', '2', '3', '4', '5', '6', '7'):
            input_ok = True
        else:
            print('Invalid input. Selection(must be 1-7)')
    print('-' * 45)
    # noinspection PyUnboundLocalVariable
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input first number: ')
    num2 = get_integer_input('Input second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


finished = False
while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    elif menu_choice == '5':
        result = integer_division(n1, n2)
    elif menu_choice == '6':
        result = modulus(n1, n2)
    elif menu_choice == '7':
        result = exponent(n1, n2)
    print('Result:', result)
    print("=" * 15)
    finished = check_if_user_has_finished()

print('See you soon Mathematician')
print('Have a nice one')

