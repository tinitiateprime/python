# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Set Comprehensions
#  Author       : Team Tinitiate
# ==============================================================================



numbers = {1, 2, 3, 4, 5}
squared_numbers = {x ** 2 for x in numbers}  
print(squared_numbers)
# OUTPUT: {1, 4, 9, 16, 25}
