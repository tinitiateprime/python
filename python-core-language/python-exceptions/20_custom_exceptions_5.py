#
# Custom Exceptions in Python
# Author: __author_credits__



class CustomError(Exception):
    pass

def process_data(data):
    if not data:
        raise CustomError("No data provided!")

try:
    process_data(None)
except CustomError as ce:
    print(ce)
# Output: No data provided!