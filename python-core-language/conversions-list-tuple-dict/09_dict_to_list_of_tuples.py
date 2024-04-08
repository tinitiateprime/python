#
# Converting Dictionary to List of Tuples in Python
# Author: __author_credits__



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}

list_of_tuples = list(my_dict.items())
print(list_of_tuples)  
# Output: [('name', 'John'), ('age', 30), ('gender', 'Male')]