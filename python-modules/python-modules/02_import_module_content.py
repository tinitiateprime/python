#
# Using a Module In Python
# Author: __author_credits__



from my_module import country_1, dictionary_world_nations, module_function_add
# This imports only country_1 variable,
# dictionary_world_nations dictionary variable and module_function_add function

# We can use the imported objects directly without using
# the syntax module_name.object_name
# Print the "my_module" variables
print (country_1);

# Uncomment and try to use not imported object, will give an error
# print (country_2);

# print the "my_module" DICTIONARY
print (dictionary_world_nations);

# Calling a function from the "my_module"
print (module_function_add(1, 3));

# Output: USA
#         {'Country_1': 'Brazil', 'Country_2': 'Germany', 'Country_3': 'Japan'}
#         4