#
# Accessing Elements in Nested Tuples in Python
# Author: __author_credits__



my_nested_tuple = ((1, 2), (11, 22), (111, 222))
#                    0       1          2
#                  00  01   10  11    20    21

# First tuple
print(my_nested_tuple[0])       # Output: (1, 2)
# First tuple elements
print(my_nested_tuple[0][0])    # Output: 1
print(my_nested_tuple[0][1])    # Output: 2

# Last tuple
print(my_nested_tuple[2])       # Output: (111, 222)
# Last tuple elements
print(my_nested_tuple[2][0])    # Output: 111
print(my_nested_tuple[2][1])    # Output: 222

# Last tuple using negative indexing
print(my_nested_tuple[-1])      # Output: (111, 222)
# Last tuple elements using negative indexing
print(my_nested_tuple[-1][-2])  # Output: 111
print(my_nested_tuple[-1][-1])  # Output: 222