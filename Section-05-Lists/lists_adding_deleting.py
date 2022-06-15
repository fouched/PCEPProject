"""
Add and delete elements in a list
"""
my_list = [6, 7, 8, 9, 10]
my_list.append(11)
print(my_list)
# add element at index 3, rest gets moved on
my_list.insert(3, 12)
print(my_list)
# removes any element with value of 12
my_list.remove(12)
print(my_list)
# removes element at element
my_list.pop(2)
print(my_list)

my_list.reverse()
print(my_list)

my_list = [10, 18, 20, 3, 4, 5, 15]
my_list.sort()
print(my_list)