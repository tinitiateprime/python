#
# Functions with a LIST input parameter in Python
# Author: __author_credits__



def process_list(input_list):
    """
    Process a list of numbers.

    Args:
        input_list (list): A list of numbers.

    Returns:
        list: A list containing squared numbers.
    """
    squared_numbers = [x ** 2 for x in input_list]
    return squared_numbers

# Calling the function 
numbers = [1, 2, 3, 4, 5]
result = process_list(numbers)
print("Squared numbers:", result)
# Output: Squared numbers: [1, 4, 9, 16, 25]