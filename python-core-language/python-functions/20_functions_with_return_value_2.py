#
# Functions with Return Value in Python
# Author: __author_credits__



def calculate_average(numbers):
    """
    Calculate the average of numbers in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Call the function
numbers_list = [1, 2, 3, 4, 5]
average = calculate_average(numbers_list)
print("Average:", average)
# Output: Average: 3.0