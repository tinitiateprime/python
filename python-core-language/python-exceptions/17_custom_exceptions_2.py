#
# Custom Exceptions in Python
# Author: __author_credits__



class tinitiate_exception(Exception):pass

# Block to test the user defined exception
try:
    raise tinitiate_exception
except tinitiate_exception:
    print("This is a user defined exception !")
# Output: This is a user defined exception !