#
# Handling Multiple Exceptions in Python
# Author: __author_credits__



try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Error: Please enter valid integers")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except Exception as e:
    print("An error occurred:", e)

# Input 1: a
# Input 2: 1 
# Output: Error: Please enter valid integers

# Input 1: 1
# Input 2: 0
# Output: Error: Division by zero is not allowed