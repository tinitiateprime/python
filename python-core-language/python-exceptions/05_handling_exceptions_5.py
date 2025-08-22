# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    v = 1/0
except Exception as e:
    print(type(e).__name__, e)
# type() function returns the type of the specified object as a type object.
# type(e).__name__ prints the name of the exception class
# e prints the actual exception instance
# OUTPUT: ZeroDivisionError division by zero
