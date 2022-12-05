course = "Learning python's from beginning"
print(course)

whatLearned = 'Learned python "print()" , "input()" and "variables"'
print(whatLearned)

# Multiple line print
emailText = '''
Hi team,
I'm learning python from beginning, it will take time to create POC.

Thank you,
The support team
'''
print(emailText)

strIndex = 'Python'
print(strIndex[0])
print(strIndex[-1])
print(strIndex[0:3])
print(strIndex[0:])
print(strIndex[1:])
print(strIndex[:3])

copyValue = strIndex[:]
print(copyValue)

name = 'MohanBabu'
print(name[1:-1])

firstName = 'Mohan'
lastName = 'babu'
concatString = firstName + ' [' + lastName + '] ' + 'is a coder'
formattedString = f'{firstName} [{lastName}] is a coder'
print(concatString)
print(formattedString)
