#
# Default Arguments Functions in Python
# Author: __author_credits__



def function_with_default_arguments( arg1, default_arg2 = 100 ):
    "This is a demonstration for default argument"
    print("Value of arg1: ", arg1)
    print("Value of default_arg2: ", default_arg2)
    return      # If Nothing specified returns None

# Calling function with both arguments 
print(function_with_default_arguments( arg1 = 10, default_arg2 = 99 ))
# OUTPUT:
#    Value of arg1:  10
#    Value of default_arg2:  99
#    None

# Calling function with ONLY ONE argument
print(function_with_default_arguments( arg1 = 11))
# OUTPUT:
#    Value of arg1:  11
#    Value of default_arg2:  100
#    None