#
# Converting List to Dictionary in Python
# Author: __author_credits__



my_list = ['name', 'John', 'age', 30, 'gender', 'Male']
print(my_list)
# Output: ['name', 'John', 'age', 30, 'gender', 'Male']

my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}
print(my_dict)  
# Output: {'name': 'John', 'age': 30, 'gender': 'Male'}