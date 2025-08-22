# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Multiple Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
# INPUT : 0
# OUTPUT: Invalid input or division by zero.
