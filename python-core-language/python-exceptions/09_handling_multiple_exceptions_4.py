# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Multiple Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



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
# INPUT 1: a
# INPUT 2: 1 
# OUTPUT : Error: Please enter valid integers

# INPUT 1: 1
# INPUT 2: 0
# OUTPUT : Error: Division by zero is not allowed
