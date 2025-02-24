# Remove an item from a tuple
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
my_list.remove(3)  # Remove item 3
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 4, 5)
