#
# Scope of Variables in Functions in Python
# Author: __author_credits__



global_variable = 10  # Global variable
def func():
    local_variable = 20  # Local variable
    print(global_variable)  # Accessing global variable inside function
    print(local_variable)

func()
print(global_variable)  # Accessing global variable outside function
# Output: 10
#         20
#         10

# print(local_variable)  # Uncomment and run, This line would raise an error