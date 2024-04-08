#
# Scope of Variables in Functions in Python
# Author: __author_credits__



MyVar = 'This is a Global Value'
def myFunction():
    # Local Variable
    MyVar = 'This is a local variable'
    print('Value of MyVar inside function: ', MyVar)

# Make a call to myFunction
myFunction()
print('Value of MyVar outside function: ', MyVar)

# Output: Value of MyVar inside function:  This is a local variable
#         Value of MyVar outside function:  This is a Global Value