#
# Handling Multiple Exceptions in Python
# Author: __author_credits__



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
# Output: An error occurred 2: