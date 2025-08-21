# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Dictionary Methods
#  Author       : Team Tinitiate
# ==============================================================================



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}



# keys()
print(my_dict.keys())  
# OUTPUT: dict_keys(['name', 'age', 'gender'])



# values()
print(my_dict.values())  
# OUTPUT: dict_values(['John', 30, 'Male'])



# items()
print(my_dict.items())   
# OUTPUT: dict_items([('name', 'John'), ('age', 30), ('gender', 'Male')])



# pop()
value = my_dict.pop('age')
print(value)  
# OUTPUT: 30
print(my_dict)  
# OUTPUT: {'name': 'John', 'gender': 'Male'}



# popitem()
key, value = my_dict.popitem()
print(key, value)  
# OUTPUT: gender Male
print(my_dict)     
# OUTPUT: {'name': 'John'}
