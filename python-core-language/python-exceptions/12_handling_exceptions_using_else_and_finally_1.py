#
# Handling Exceptions Using `else` and `finally` in Python
# Author: __author_credits__



try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)
finally:
    print("Execution complete")
    
# Output: Result: 5.0
#         Execution complete