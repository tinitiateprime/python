#
# Handling Exceptions in Python
# Author: __author_credits__



try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError:
    print("Error: Key not found")
# Output: Error: Key not found