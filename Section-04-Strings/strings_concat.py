"""
Strings concatenation
"""
my_name = 'Fouche'
print(my_name + ' du Preez')

# Formats
number_of_shoes = 8
# cannot concat other variable types
# print(my_name + ' has ' + number_of_shoes + ' number of shoes')

text_1 = '{} has {} number of shoes'.format(my_name, number_of_shoes)
print(text_1)

# most popular way...
text_2 = f'{my_name} has {number_of_shoes} number of shoes'
print(text_2)


