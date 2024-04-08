#
# Handling Exceptions Using `else` and `finally` in Python
# Author: __author_credits__



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
finally:
    print("Execution complete.")

# Input : 2
# Output: Result: 5.0
#         Execution complete.

# Input : 0
# Output: Division by zero is not allowed.
#         Execution complete.