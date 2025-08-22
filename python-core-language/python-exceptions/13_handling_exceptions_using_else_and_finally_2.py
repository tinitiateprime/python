# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions Using `else` and `finally`
#  Author       : Team Tinitiate
# ==============================================================================



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")
# INPUT : 2
# OUTPUT: Result: 5.0
#         Execution complete.

# INPUT : 0
# OUTPUT: Division by zero is not allowed.
#         Execution complete.
