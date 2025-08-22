# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Scope of Variables in Functions
#  Author       : Team Tinitiate
# ==============================================================================



global_variable = 10  # Global variable
def func():
    local_variable = 20  # Local variable
    print(global_variable)  # Accessing global variable inside function
    print(local_variable)

func()
print(global_variable)  # Accessing global variable outside function
# OUTPUT: 10
#         20
#         10

# print(local_variable)  # Uncomment and run, This line would raise an error
