# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    # Code that might raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the exception
    print("Error: Division by zero")
# OUTPUT: Error: Division by zero
