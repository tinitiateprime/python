# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Looping Through Dictionary
#  Author       : Team Tinitiate
# ==============================================================================



my_dict = {"name": "John", "age": 30, "gender": "Male"}

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)
# OUTPUT: name
#         age
#         gender
#         John
#         30
#         Male
#         name John
#         age 30
#         gender Male
