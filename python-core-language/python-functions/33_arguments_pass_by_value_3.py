# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Arguments Pass By Value
#  Author       : Team Tinitiate
# ==============================================================================



def modify_tuple(t):
    t = (4, 5, 6)
    print(t)

my_tuple = (1, 2, 3)
modify_tuple(my_tuple)
print(my_tuple)  
# OUTPUT: (4, 5, 6)
#         (1, 2, 3)
