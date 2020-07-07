number_check = input('Number: ')

if number_check.isnumeric():
    new_number = int(number_check)

    if new_number <= 2:
        print('Number must be greater than 2')
    else:
        prime_number = True
        for i in range(2, new_number):
            for j in range(2, i):
                if i % j == 0:
                    prime_number = False
                    break
            if prime_number:
                print('Prime number', i)
            prime_number = True
else:
    print('Number entered must be a positive integer')
