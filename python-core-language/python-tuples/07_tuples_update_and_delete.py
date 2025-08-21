# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Tuple Update and Delete
#  Author       : Team Tinitiate
# ==============================================================================



tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('A', 'b', 1, 2)

# UPDATE TUPLES
# Easier option for updating parts of tuple are creating 
# new tuples with parts of existing ones
# Create a Tuple with elements 2,3,4 from tuple1
tuple3=tuple1[1:4]
print(tuple3)
# Output: (2, 3, 4)

# DELETING TUPLES 
del tuple3
# print(tuple3) # This will throw an error, as this TUPLE doesnt exist
