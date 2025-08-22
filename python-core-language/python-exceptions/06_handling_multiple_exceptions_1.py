# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Multiple Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ValueError:
    # Handle ValueError
    print("An error occurred 1:")
except ZeroDivisionError:
    # Handle ZeroDivisionError
    print("An error occurred 2:")
except Exception as e:
    # Catch all other exceptions
    print("An error occurred3 :", e)
# OUTPUT: An error occurred 2:
