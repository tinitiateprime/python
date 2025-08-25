# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Executable and Import Module Caller
#  Author       : Team Tinitiate
# ==============================================================================



import addition_module

# Using the function from the module with default values
result_default = addition_module.add_variables()
print(f"Default sum is: {result_default}")

# Using the function from the module with custom values
value3 = 5
value4 = 3
result_custom = addition_module.add_variables(value3, value4)
print(f"Custom sum is: {result_custom}")
# OUTPUT: Default sum is: 0
#         Custom sum is: 8
