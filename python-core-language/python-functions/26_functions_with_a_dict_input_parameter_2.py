#
# Functions with a DICTIONARY input parameter in Python
# Author: __author_credits__



def calculate_average_values(input_dict):
    """
    Calculate the average of values for each key in a dictionary.

    Args:
        input_dict (dict): A dictionary with keys mapped to lists of numbers.

    Returns:
        dict: A dictionary containing keys and their corresponding averages.
    """
    average_dict = {}
    for key, values in input_dict.items():
        average = sum(values) / len(values)
        average_dict[key] = average
    return average_dict

# Calling the function
data = {
    "A": [10, 20, 30],
    "B": [15, 25, 35],
    "C": [20, 30, 40]
}
averages = calculate_average_values(data)
print("Average values:", averages)
# Output: Average values: {'A': 20.0, 'B': 25.0, 'C': 30.0}