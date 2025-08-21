# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : List to Dictionary
#  Author       : Team Tinitiate
# ==============================================================================



my_list = ['name', 'John', 'age', 30, 'gender', 'Male']
print(my_list)
# OUTPUT: ['name', 'John', 'age', 30, 'gender', 'Male']

my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(my_dict)  
# OUTPUT: {'name': 'John', 'age': 30, 'gender': 'Male'}
