# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Accessing Nested Dictionary Elements
#  Author       : Team Tinitiate
# ==============================================================================



# Nested dict variation 1
my_dict = {'person': {'name': 'John', 'age': 30}}

print(my_dict)
# OUTPUT: {'person': {'name': 'John', 'age': 30}}

print(my_dict['person'])
# OUTPUT: {'name': 'John', 'age': 30}

print(my_dict['person']['name'])  
# OUTPUT: John

print(my_dict['person']['age'])   
# OUTPUT: 30



# Nested dict variation 2
list_dict = [{'EmpID':1, 'EmpName':'Venkat'},
             {'EmpID':2, 'EmpName':'Sujatha'},
             {'EmpID':3, 'EmpName':'Taran'}]

# Print Name of EmpID: 3 using indexing
# EmpID: 3 is 3rd element, whose index is "2"
print(list_dict[2]['EmpName'])
# OUTPUT: Taran
