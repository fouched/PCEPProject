"""
Sets - Unique and not repeated values
Faster than lists if you want to check if an item is in it
Looping of lists are faster
NOT ordered
"""

my_set = {'apples', 'bananas', 'oranges', 'melons'}
print(my_set)

print('apples' in my_set)
print('grape' in my_set)

for x in my_set:
    print(x)

# remove - will error if element does not exist
my_set.remove('apples')
# remove without error
my_set.discard('grapes')
print(my_set)
# clear
my_set.clear()
print(my_set)
# combine sets
set_one = {1, 2, 3}
set_two = {4, 5, 6}
set_three = set_one.union(set_two)
print(set_three)
# add
set_three.add('Pear')
print(set_three)

# add multiple
set_three.update(['Mango', 'Grapes', 'Banana'])
print(set_three)
