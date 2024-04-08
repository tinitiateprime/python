#
# Custom Exceptions in Python
# Author: __author_credits__



class CustomError(Exception):
    pass

try:
    raise CustomError("An error occurred")
except CustomError as e:
    print("Custom error:", e)
# Output: Custom error: An error occurred