#
# Handling Exceptions Using `finally` in Python
# Author: __author_credits__



try:
    v = 1/1  # Trying to Divide By zero
except ZeroDivisionError:
    print("Tinitiate: Cannot Divide by ZERO")
finally:
    print("Tinitiate: THIS MESSAGE MUST BE PRINTED")
# Output: Tinitiate: THIS MESSAGE MUST BE PRINTED