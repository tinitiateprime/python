# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Dictionary to List of Keys or Values
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
