#
# Functions with loop and conditional statements in Python
# Author: __author_credits__



def function_with_constructs(in_string, in_number):
    "This function demonstrates use of loop and conditional statements"
    # Loop
    for c in range(5):
        print(in_string)

    # Conditional statement
    if in_number%2 == 0:
        print(in_number,' is even.')
    elif in_number%2 != 0:
        print(in_number,' is odd.')

# Calling the function
function_with_constructs("Python", 20)
# OUTPUT:
#    Python
#    Python
#    Python
#    Python
#    Python
#    20 is even.