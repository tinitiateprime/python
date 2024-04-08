#
# Handling Exceptions in Python
# Author: __author_credits__



try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero")
# Output: Error: Division by zero