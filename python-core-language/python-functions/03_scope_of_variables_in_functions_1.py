#
# Scope of Variables in Functions in Python
# Author: __author_credits__



def my_func():
    x = 10 # Local Variable
    print("Inside function:", x)

x = 20 # Global Variable
my_func()
print("Outside function:", x)

# Output: Inside function: 10
#         Outside function: 20