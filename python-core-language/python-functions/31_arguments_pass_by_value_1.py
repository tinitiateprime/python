# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Value
#  Author       : Team Tinitiate
# ==============================================================================



def modify_number(num):
    num = num + 1  # Modifying the number inside the function
    print(num)

my_num = 5

modify_number(my_num) 
# OUTPUT: 6

print(my_num)  
# OUTPUT: 5
