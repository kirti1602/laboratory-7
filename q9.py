# Find repeated items in a tuple
my_tuple = (1, 2, 2, 3, 4, 4, 5)
repeated = []
for i in my_tuple:
    if my_tuple.count(i) > 1 and i not in repeated:
        repeated.append(i)
print(repeated)  # Output: [2, 4]
