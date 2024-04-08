#
# Handling Multiple Exceptions in Python
# Author: __author_credits__



try:
    value = int(input("Enter a number: "))
    result = 10 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")

# Input: 0
# Output: Invalid input or division by zero.