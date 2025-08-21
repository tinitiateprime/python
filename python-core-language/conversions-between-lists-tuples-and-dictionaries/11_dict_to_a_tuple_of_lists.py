# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Dictionary to a Tuple of Lists
#  Author       : Team Tinitiate
# ==============================================================================



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# OUTPUT: {'name': 'John', 'age': 30, 'gender': 'Male'}

keys_list = list(my_dict.keys())
print(keys_list)  
# OUTPUT: ['name', 'age', 'gender']

values_list = list(my_dict.values())
print(values_list)  
# OUTPUT: ['John', 30, 'Male']

tuple_of_lists = (keys_list, values_list)
print(tuple_of_lists) 
# OUTPUT: (['name', 'age', 'gender'], ['John', 30, 'Male'])
