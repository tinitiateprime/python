#
# Executable and Import Module Caller In Python
# Author: __author_credits__



import addition_module

# Using the function from the module with default values
result_default = addition_module.add_variables()
print(f"Default sum is: {result_default}")

# Using the function from the module with custom values
value3 = 5
value4 = 3
result_custom = addition_module.add_variables(value3, value4)
print(f"Custom sum is: {result_custom}")

# Output: Default sum is: 0
#         Custom sum is: 8