# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Handling Exceptions
#  Author       : Team Tinitiate
# ==============================================================================



try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Error: Index out of range")
# OUTPUT: Error: Index out of range
