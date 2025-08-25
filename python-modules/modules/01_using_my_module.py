# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using a Module
#  Author       : Team Tinitiate
# ==============================================================================



import my_module
# Imports the "my_module" module

# To use objects of my_module, use the syntax module_name.object_name
# Print the "my_module" variables
print (my_module.country_1, my_module.country_2, my_module.country_3);

# Print the "my_module" LIST
print (my_module.list_world_nations);

# print the "my_module" TUPLE
print (my_module.tuple_world_nations);

# print the "my_module" DICTIONARY
print (my_module.dictionary_world_nations);

# Calling a function from the "my_module"
print (my_module.module_function_add(1, 3));
# OUTPUT: USA China India
#         ['Argentina', 'Italy', 'Australia']
#         ('Spain', 'France', 'Canada')
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4
