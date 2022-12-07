command = ''
started = False
print('Type help to get details of car game...')
while command.lower() != 'quit':
    command = input('> ')
    if command.lower() == 'start':
        if started:
            print('Car already in start')
        else:
            started = True
            print('Car started... ready to go')
    elif command.lower() == 'stop':
        print('Car stopped.')
    elif command.lower() == 'quit':
        break
    elif command.lower() == 'help':
        print('''
    start -> to start the car...
    stop -> to stop the car...
    quit -> to exit car game!
''')
    else:
        print('I don"t understand that...')
