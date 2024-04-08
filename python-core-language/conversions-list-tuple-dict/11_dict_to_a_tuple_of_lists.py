#
# Converting Dictionary to a Tuple of Lists in Python
# Author: __author_credits__



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

keys_list = list(my_dict.keys())
print(keys_list)  
# Output: ['name', 'age', 'gender']

values_list = list(my_dict.values())
print(values_list)  
# Output: ['John', 30, 'Male']

tuple_of_lists = (keys_list, values_list)
print(tuple_of_lists) 
# Output: (['name', 'age', 'gender'], ['John', 30, 'Male'])