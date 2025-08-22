# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



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
# OUTPUT: Custom error: An error occurred
#         Error code: 500
