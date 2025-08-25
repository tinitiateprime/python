from . import add_variables
from . import multiply_variables

def main():
    # Using the add_variables function from MathModule
    value1 = int(input("Enter the first number for addition: "))
    value2 = int(input("Enter the second number for addition: "))
    result_add = add_variables.add_variables(value1, value2)
    print(f"The sum is: {result_add}")

    # Using the multiply_variables function from MathModule
    value3 = int(input("Enter the first number for multiplication: "))
    value4 = int(input("Enter the second number for multiplication: "))
    result_multiply = multiply_variables.multiply_variables(value3, value4)
    print(f"The product is: {result_multiply}")

if __name__ == "__main__":
    # This block will only execute if this script (__main__.py) is run directly.
    main()
# OUTPUT: Enter the first number for addition: 1
#         Enter the second number for addition: 2
#         The sum is: 3
#         Enter the first number for multiplication: 3
#         Enter the second number for multiplication: 4
#         The product is: 12
