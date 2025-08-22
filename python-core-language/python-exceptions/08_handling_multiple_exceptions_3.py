# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Multiple Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]  # This will raise a KeyError
    my_list = [1, 2, 3]
    print(my_list[4])  # This will raise an IndexError
except (KeyError, IndexError):
    print("Error: Key not found or index out of range")
# OUTPUT: Error: Key not found or index out of range
