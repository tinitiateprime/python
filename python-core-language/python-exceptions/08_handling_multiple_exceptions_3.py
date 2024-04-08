#
# Handling Multiple Exceptions in Python
# Author: __author_credits__



try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]  # This will raise a KeyError
    my_list = [1, 2, 3]
    print(my_list[4])  # This will raise an IndexError
except (KeyError, IndexError):
    print("Error: Key not found or index out of range")
# Output: Error: Key not found or index out of range