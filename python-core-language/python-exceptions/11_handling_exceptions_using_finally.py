# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions Using `finally`
#  Author       : Team Tinitiate
# ==============================================================================



try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")
# OUTPUT: Tinitiate: THIS MESSAGE MUST BE PRINTED
