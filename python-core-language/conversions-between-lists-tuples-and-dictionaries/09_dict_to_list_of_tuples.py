# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Dictionary to List of Tuples
#  Author       : Team Tinitiate
# ==============================================================================



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}
print(my_dict)
# OUTPUT: {'name': 'John', 'age': 30, 'gender': 'Male'}

list_of_tuples = list(my_dict.items())
print(list_of_tuples)  
# OUTPUT: [('name', 'John'), ('age', 30), ('gender', 'Male')]
