#
# Handling Exceptions in Python
# Author: __author_credits__



try:
    v = 1/0
except Exception as e:
    print(type(e).__name__, e)
# type() function returns the type of the specified object as a type object.
# type(e).__name__ prints the name of the exception class
# e prints the actual exception instance
# Output: ZeroDivisionError division by zero