# temp = input('Enter room temperature? ')
# if int(temp) > 30:
#     print('Its a hot day')
# else:
#     print('Its a cold day')

name = input('Enter your name? ')
if len(name) < 3:
    print('Name must be at-least 3 char')
elif len(name) > 50:
    print('Name must be less then 50 char')
else:
    print('name looks good')