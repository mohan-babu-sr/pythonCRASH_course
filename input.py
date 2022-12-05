name = input('What is your name? ')
color = input('What is your fav color? ')
print(name + ' likes ' + color)

birthYear = input('What is your birth year ')
age = 2022 - int(birthYear)
print('Your age is ' + str(age))

weight_pounds = input('Enter your weight in pounds? ')
weight_kg = float(weight_pounds)/2.205
print('Your weight in kg ' + str(round(weight_kg, 2)))
