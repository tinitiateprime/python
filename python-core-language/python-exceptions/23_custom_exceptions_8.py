#
# Custom Exceptions in Python
# Author: __author_credits__



# Custom exception with additional attributes
class CustomError(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

try:
    raise CustomError("An error occurred", 500)
except CustomError as e:
    print("Custom error:", e)
    print("Error code:", e.code)
# Output: Custom error: An error occurred
#         Error code: 500