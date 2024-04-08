#
# Functions Pass By Reference in Python
# Author: __author_credits__



def add_key_value(my_dict):
    my_dict["c"] = 30
    print(my_dict)

data = {"a": 10, "b": 20}

add_key_value(data) 
# Output: {'a': 10, 'b': 20, 'c': 30}

print(data)  
# Output: {'a': 10, 'b': 20, 'c': 30}