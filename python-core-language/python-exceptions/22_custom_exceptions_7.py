# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



class CustomError(Exception):
    pass

try:
    raise CustomError("An error occurred")
except CustomError as e:
    print("Custom error:", e)
# OUTPUT: Custom error: An error occurred
