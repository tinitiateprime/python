# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Reference
#  Author       : Team Tinitiate
# ==============================================================================



def modify_list(my_list):
    my_list.append(4)
    my_list[0] = 100
    print(my_list) 

numbers = [1, 2, 3]

modify_list(numbers) 
# OUTPUT: [100, 2, 3, 4]

print(numbers)  
# OUTPUT: [100, 2, 3, 4]
