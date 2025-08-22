# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Loop Control Statements
#  Author       : Team Tinitiate
# ==============================================================================



# break
cur_value = 0                  
while (cur_value < 5):
    cur_value += 1 
    if cur_value==3:
        break
    print('Cur_value: ', cur_value)
# OUTPUT: Cur_value:  1
#         Cur_value:  2
