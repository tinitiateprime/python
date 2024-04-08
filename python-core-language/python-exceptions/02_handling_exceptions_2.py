#
# Handling Exceptions in Python
# Author: __author_credits__



try:
    result = "10" / 2
except TypeError:
    print("Error: Unsupported operand type(s) for /: 'str' and 'int'")
# Output: Error: Unsupported operand type(s) for /: 'str' and 'int'