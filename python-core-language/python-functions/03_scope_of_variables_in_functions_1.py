# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Scope of Variables in Functions
#  Author       : Team Tinitiate
# ==============================================================================



def my_func():
    x = 10 # Local Variable
    print("Inside function:", x)

x = 20 # Global Variable
my_func()
print("Outside function:", x)
# OUTPUT: Inside function: 10
#         Outside function: 20
