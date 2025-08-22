# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Define and call a Function
#  Author       : Team Tinitiate
# ==============================================================================



# Defining a Function
def square(number):
    """Calculate the square of a number."""
    result = number ** 2
    return result

# Calling a Function
num = 5
square_result = square(num)
print(f"The square of {num} is {square_result}")
# OUTPUT: The square of 5 is 25
