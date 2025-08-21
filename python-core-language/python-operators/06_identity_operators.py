# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Identity Operators
#  Author       : Team Tinitiate
# ==============================================================================



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

# is
print(x is y)     # Output: False 
                  #(Different objects, even though they have the same values)
print(x is z)     # Output: True (Same object, assigned to z)

# is not
print(x is not y) # Output: True
