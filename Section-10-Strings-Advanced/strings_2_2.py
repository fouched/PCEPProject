greetings = 'Welcome to the Python world!'

# Joins
print(greetings, ','.join('abcdefg'))
print(greetings, ':'.join(('10', '23', '15')))

password = '   abc123!   '
if password.strip() == 'abc123!':
    print('Password success')
else:
    print('Password incorrect')

new_greetings = greetings.replace('Welcome to', 'Hello there! Welcome to')
print(new_greetings)
