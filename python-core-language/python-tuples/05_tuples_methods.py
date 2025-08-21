# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Tuple Methods
#  Author       : Team Tinitiate
# ==============================================================================



my_tuple = (1, 2, 3, 2)

# count()
print(my_tuple.count(2))  
# Output: 2 (number of occurrences of 2)

# index()
print(my_tuple.index(3))  
# Output: 2 (index of the first occurrence of 3)

# min() and max()
print("Min =",min(my_tuple), "Max =",max(my_tuple)) 
# Output: Min = 1 Max = 3

# len()
print(len(my_tuple)) 
# Output: 4

# sum()
print(sum(my_tuple)) 
# Output: 8
