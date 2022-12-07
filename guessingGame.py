import random
i = 0
while i < 3:
    secretNumber = random.randint(0, 10)
    i += 1
    userNumber = input('Guess the number : ')
    if int(userNumber) == int(secretNumber):
        print('You win!')
        break
    else:
        print('Secret Number ' + str(secretNumber))
        print('Try again to win')
print('Limit reached..!')
