#
# Functions Pass By Reference in Python
# Author: __author_credits__



source_list = ['A', 'B', 'C']

def function_pass_by_reference(in_list):
    print('function_pass_by_reference says Input List: ', in_list)
    # Changing the input by appending a value to in_list
    in_list.append('D')
    print('function_pass_by_reference says changed List: ', in_list)

print('Before passing reference to function, source_list: ', source_list)

# Passing the "source_list" and NOT A COPY of the "source_list"
function_pass_by_reference(source_list)
print('After passing reference to function, source_list: ', source_list)

# Ouput:
# Before passing reference to function, source_list:  ['A', 'B', 'C']
# function_pass_by_reference says Input List:  ['A', 'B', 'C']
# function_pass_by_reference says changed List:  ['A', 'B', 'C', 'D']
# After passing reference to function, source_list:  ['A', 'B', 'C', 'D']