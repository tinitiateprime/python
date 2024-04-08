#
# Functions Pass By Value in Python
# Author: __author_credits__



# Create a source list
source_list_2 = ['A', 'B', 'C']

def function_pass_by_value(in_list):
    print('function_pass_by_value says Input List: ', in_list)
    # Reassigning a local value, [pass by value]
    in_list =[1, 2, 3, 4]
    print('function_pass_by_value says changed List: ', in_list)

print('Before passing by value to function, source_list: ', source_list_2)

function_pass_by_value(source_list_2)

print('After passing by value to function, source_list: ', source_list_2)

# Output:
# Before passing by value to function, source_list:  ['A', 'B', 'C']
# function_pass_by_value says Input List:  ['A', 'B', 'C']
# function_pass_by_value says changed List:  [1, 2, 3, 4]
# After passing by value to function, source_list:  ['A', 'B', 'C']