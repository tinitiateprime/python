# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Scope of Variables in Functions
#  Author       : Team Tinitiate
# ==============================================================================



MyVar = 'This is a Global Value'
def myFunction():
    # Local Variable
    MyVar = 'This is a local variable'
    print('Value of MyVar inside function: ', MyVar)

# Make a call to myFunction
myFunction()
print('Value of MyVar outside function: ', MyVar)
# OUTPUT: Value of MyVar inside function:  This is a local variable
#         Value of MyVar outside function:  This is a Global Value
