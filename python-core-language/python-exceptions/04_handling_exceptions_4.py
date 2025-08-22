# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    my_dict = {"a": 1, "b": 2}
    value = my_dict["c"]
except KeyError:
    print("Error: Key not found")
# OUTPUT: Error: Key not found
