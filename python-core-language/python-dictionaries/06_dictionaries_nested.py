#
# Nested Dictionaries in Python
# Author: __author_credits__


# Nested dict variation 1
my_dict = {'person': {'name': 'John', 'age': 30}}

print(my_dict)
# Output: {'person': {'name': 'John', 'age': 30}}

print(my_dict['person'])
# Output: {'name': 'John', 'age': 30}

print(my_dict['person']['name'])  
# Output: John

print(my_dict['person']['age'])   
# Output: 30


# Nested dict variation 2
list_dict = [{'EmpID':1, 'EmpName':'Venkat'},
             {'EmpID':2, 'EmpName':'Sujatha'},
             {'EmpID':3, 'EmpName':'Taran'}]

# Print Name of EmpID: 3 using indexing
# EmpID: 3 is 3rd element, whose index is "2"
print(list_dict[2]['EmpName'])
# Output: Taran