#
# Reassigning a variable and Deleting a variable in Python
# Author: __author_credits__



variable1 = 1;          # Integer
variable2 = "test";     # String
variable3 = 100.4;      # float value

# Reassign a value to a variable
variable1 = 4;          # Integer
print("variable1 reassigned value: ", variable1)
# Reassign a variable value to a variable
variable1 = variable2
print("variable1 again reassigned value: ", variable1)

# Deleting a single or multiple variables by using the del statement.
del variable1
# Use comma(,) after variable for multiple deletes
# Using the variable after deleting will raise an error
# Remove comment symbol (#) and try to print the below statement,
# it will raise an error
# print("variable1 reassigned value: ", variable1)


# OUTPUT
# variable1 reassigned value:  4
# variable1 again reassigned value:  test