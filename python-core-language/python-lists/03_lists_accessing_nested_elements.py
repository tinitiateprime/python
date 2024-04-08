#
# Accessing Elements in Nested Lists in Python
# Author: __author_credits__



nested_list = [[1, 2], [3, 4], [5, 6]]
#                0        1      2
#              00  01   10 11   20 21 
# First list in nested_list
print(nested_list[0])       # Output: [1, 2]
# First list elements in nested_list
print(nested_list[0][0])    # Output: 1
print(nested_list[0][1])    # Output: 2

# Second list in nested_list
print(nested_list[1])       # Output: [3, 4]
# First list elements in nested_list
print(nested_list[1][0])    # Output: 3
print(nested_list[1][1])    # Output: 4

# Third list in nested_list
print(nested_list[2])       # Output: [5, 6]
# First list elements in nested_list
print(nested_list[2][0])    # Output: 5
print(nested_list[2][1])    # Output: 6