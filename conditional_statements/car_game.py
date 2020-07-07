def car_game():
    command = ""
    started = False
    while True:
        command = input('> ').lower()
        if command == 'start':
            if started:
                print('Car already started')
            else:
                started = True
                print('Vruum! vruum! ...Car started')
        elif command == 'stop':
            if not started:
                print('Car is already stopped')
            else:
                started = False
                print('Car coming to a stop....car has stopped')
        elif command == 'help':
            print("""start - To start your car
stop - To bring your car to a halt
help - For help with the game
quit - To exit the game""")
        elif command == 'quit':
            print('You have exited the game ...see you soon')
            break
        else:
            print('Wrong command entered')

car_game()
