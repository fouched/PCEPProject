user_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_year': 1990
}

for x in user_dict:
    print(x)


for x, y in user_dict.items():
    print(x, y)

if 'birth_year' in user_dict:
    print('birth_year exists!')

# Copy
dict2 = user_dict.copy()
dict2.popitem()
print(f'user_dict {user_dict}')
print(f'dict2 {dict2}')

# Nested
family = {
    'child1': {
        'first_name': 'John',
        'last_name': 'Doe',
        'birth_year': 1990
    },
    'child2': {
        'first_name': 'Mary',
        'last_name': 'Doe',
        'birth_year': 1993
    },
    'child3': {
        'first_name': 'Peter',
        'last_name': 'Doe',
        'birth_year': 1995
    }
}

print(family)
