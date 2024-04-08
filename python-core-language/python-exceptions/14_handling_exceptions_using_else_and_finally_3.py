#
# Handling Exceptions Using `else` and `finally` in Python
# Author: __author_credits__



try:
    x = int(input("Enter a number: "))
    result = 10 / x
    items = [1, 2, 3]
    value = items[x]
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Error: Division by zero")
except IndexError:
    print("Error: Index out of range")
else:
    print("Result:", result)
    print("Value at index", x, ":", value)
finally:
    print("Execution complete")

# Input : 2
# Output: Result: 5.0
#         Value at index 2 : 3
#         Execution complete