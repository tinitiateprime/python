# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Aliasing a Module
#  Author       : Team Tinitiate
# ==============================================================================



import my_module as m1
# Imports the "my_module" module as "m1"

# Print the "my_module" variables
print (m1.country_1, m1.country_2, m1.country_3);

# Print the "my_module" LIST
print (m1.list_world_nations);

# print the "my_module" TUPLE
print (m1.tuple_world_nations);

# print the "my_module" DICTIONARY
print (m1.dictionary_world_nations);

# Calling a function from the "my_module"
print (m1.module_function_add(1, 3));
# OUTPUT: USA China India
#         ['Argentina', 'Italy', 'Australia']
#         ('Spain', 'France', 'Canada')
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4
