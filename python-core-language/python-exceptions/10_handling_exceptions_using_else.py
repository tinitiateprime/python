# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions Using `else`
#  Author       : Team Tinitiate
# ==============================================================================



try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
else:
    print("Tinitiate: Execution completed successfully")
# OUTPUT: Tinitiate: Execution completed successfully
