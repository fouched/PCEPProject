
def remove_elements(list_of_items):
    list_of_items.pop(0)
    list_of_items.pop(-1)
    return list_of_items


number_list = [1, 2, 3, 4, 5]
mod_list = remove_elements(number_list)
print(mod_list)
