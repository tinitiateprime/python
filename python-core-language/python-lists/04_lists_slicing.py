#
# List Slicing in Python
# Author: __author_credits__



my_list = ["apple", "banana", "cherry", "date"]

# Sublist from index 1 upto 3 (not including 3)
print(my_list[1:3])   # Output: ['banana', 'cherry']

# Sublist from starting index upto 2 (not including 2)
print(my_list[:2])    # Output: ['apple', 'banana']

# Sublist from index 2 to ending index (including ending index)
print(my_list[2:])    # Output: ['cherry', 'date']