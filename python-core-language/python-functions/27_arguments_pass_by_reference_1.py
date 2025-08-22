# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Reference
#  Author       : Team Tinitiate
# ==============================================================================



def modify_list(lst):
    lst.append(4)  # Modifying the list inside the function

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  
# OUTPUT: [1, 2, 3, 4]
