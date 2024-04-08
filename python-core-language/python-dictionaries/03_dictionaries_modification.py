#
# Modifying Dictionaries in Python
# Author: __author_credits__



my_dict = {'name': 'John', 'age': 30}
print(my_dict)
# Output: {'name': 'John', 'age': 30}

# Modifying existing value
my_dict['age'] = 35
print(my_dict)
# Output: {'name': 'John', 'age': 35}

# Adding new key-value pair
my_dict['gender'] = 'Male'
print(my_dict)  
# Output: {'name': 'John', 'age': 35, 'gender': 'Male'}

# Remove the key gender and its value
del my_dict['gender'] 
print(my_dict)
# Output: {'name': 'John', 'age': 35}

# Remove everything in dictionary
my_dict.clear() 
print(my_dict)
# Output: {}