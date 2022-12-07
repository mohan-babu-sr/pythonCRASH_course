weight = input('Enter your Weight : ')
unit = input('(L)bs or (K)g : ')

if unit.lower() == 'L':
    weight = int(weight) * 0.45
    print(f'You are {weight} kilogram')
else:
    weight = int(weight) / 0.45
    print(f'You are {weight} pounds')
