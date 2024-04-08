#
# Handling Exceptions in Python
# Author: __author_credits__



try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Error: Index out of range")
# Output: Error: Index out of range