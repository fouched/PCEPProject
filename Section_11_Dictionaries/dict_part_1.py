"""
Dictionaries
A key/value collection which is unordered, changeable and indexed
"""

user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1971
}

print(user_dict)
print(user_dict['first_name'])
print(user_dict.get('last_name'))

# add to dictionary
user_dict['major'] = 'Math'
print(user_dict)

print(len(user_dict))

# remove an entry
user_dict.pop('major')
print(user_dict)
# or
del user_dict['birth_year']
print(user_dict)

# remove all entries
user_dict.clear()
print(user_dict)
