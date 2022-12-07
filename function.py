def first_function():
    print('Inside the function')


print('Start')
first_function()
print('End')


def second_function(name):
    print(f'Hi {name} welcome..!')


second_function("mohan")


def square(number):
    return number * number


squareNumber = square(4)
print(squareNumber)

try:
    age = int(input('Age : '))
    print('Your age is ' + str(age))
except ValueError:
    print('Invalid number')
