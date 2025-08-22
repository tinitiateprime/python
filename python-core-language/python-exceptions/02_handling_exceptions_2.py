# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    result = "10" / 2
except TypeError:
    print("Error: Unsupported operand type(s) for /: 'str' and 'int'")
# OUTPUT: Error: Unsupported operand type(s) for /: 'str' and 'int'
