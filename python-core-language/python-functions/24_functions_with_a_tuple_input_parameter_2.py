# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Functions with a TUPLE input parameter
#  Author       : Team Tinitiate
# ==============================================================================



def reverse_tuple(input_tuple):
    """
    Reverse the elements of a tuple.

    Args:
        input_tuple (tuple): A tuple of elements.

    Returns:
        tuple: A new tuple with elements reversed.
    """
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

# Calling the function
my_tuple = (1, 2, 3, 4, 5)
reversed_result = reverse_tuple(my_tuple)
print("Reversed tuple:", reversed_result)
# Output: Reversed tuple: (5, 4, 3, 2, 1)
