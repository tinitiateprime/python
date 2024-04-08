#
# Dictionary Methods in Python
# Author: __author_credits__



my_dict = {'name': 'John', 'age': 30, 'gender': 'Male'}

# keys()
print(my_dict.keys())  
# Output: dict_keys(['name', 'age', 'gender'])

# values()
print(my_dict.values())  
# Output: dict_values(['John', 30, 'Male'])

# items()
print(my_dict.items())   
# Output: dict_items([('name', 'John'), ('age', 30), ('gender', 'Male')])

# pop()
value = my_dict.pop('age')
print(value)  
# Output: 30
print(my_dict)  
# Output: {'name': 'John', 'gender': 'Male'}

# popitem()
key, value = my_dict.popitem()
print(key, value)  
# Output: gender Male
print(my_dict)     
# Output: {'name': 'John'}