# if condition
first_name = 'Mohan'
rating = 4.5
is_published = True
if is_published:
    print('- ' + first_name + ' have rating of ' + str(rating))

conditionValue = input('''Is weather cold or hot?
1-hot
2-cold
3-normal
input : ''')
if '1' in conditionValue:
    print('Its a hot day')
elif '2' in conditionValue:
    print('Its a cold day')
else:
    print('Its a lovely day')
