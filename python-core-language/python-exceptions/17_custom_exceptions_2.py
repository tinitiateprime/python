# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Custom Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



class tinitiate_exception(Exception):pass

# Block to test the user defined exception
try:
    raise tinitiate_exception
except tinitiate_exception:
    print("This is a user defined exception !")
# OUTPUT: This is a user defined exception !
