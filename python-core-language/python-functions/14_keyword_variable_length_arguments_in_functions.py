# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Keyword Variable-Length Arguments in Functions
#  Author       : Team Tinitiate
# ==============================================================================



def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

print_info(name="Alice", age=30, city="New York")  
# Keyword variable-length arguments: name="Alice", age=30, city="New York"
# OUTPUT: name: Alice
#         age: 30
#         city: New York
