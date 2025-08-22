# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



class CustomError(Exception):
    pass

def process_data(data):
    if not data:
        raise CustomError("No data provided!")

try:
    process_data(None)
except CustomError as ce:
    print(ce)
# OUTPUT: No data provided!
