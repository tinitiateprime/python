#
# Handling Exceptions Using `else` in Python
# Author: __author_credits__



try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
else:
    print("Tinitiate: Execution completed successfully")
# Output: Tinitiate: Execution completed successfully