# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions Using `else` and `finally`
#  Author       : Team Tinitiate
# ==============================================================================



try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)
finally:
    print("Execution complete")
# OUTPUT: Result: 5.0
#         Execution complete
